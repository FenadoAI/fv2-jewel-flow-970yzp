"""Authentication utilities for JWT and password hashing."""

import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from models import User, UserInDB, UserRole


SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

security = HTTPBearer()


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def create_access_token(user: User) -> str:
    """Create a JWT access token for a user."""
    expire = datetime.now(timezone.utc) + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode = {
        "sub": user.id,
        "email": user.email,
        "role": user.role,
        "exp": expire,
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """Decode and verify a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = None,
) -> User:
    """Get the current authenticated user from the request."""
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials
    payload = decode_token(token)

    db = request.app.state.db
    user_data = await db.users.find_one({"_id": payload["sub"]})

    if not user_data:
        raise HTTPException(status_code=401, detail="User not found")

    return User(
        id=user_data["_id"],
        username=user_data["username"],
        email=user_data["email"],
        role=user_data["role"],
        created_at=user_data["created_at"],
    )


async def get_optional_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = None,
) -> Optional[User]:
    """Get the current user if authenticated, otherwise return None."""
    if credentials is None:
        return None

    try:
        return await get_current_user(request, credentials)
    except HTTPException:
        return None


def require_role(required_role: UserRole):
    """Decorator to require a specific role or higher."""
    role_hierarchy = {"staff": 1, "manager": 2, "owner": 3}

    def check_role(user: User):
        if role_hierarchy.get(user.role, 0) < role_hierarchy.get(required_role, 999):
            raise HTTPException(
                status_code=403,
                detail=f"Insufficient permissions. Required: {required_role}+",
            )
        return user

    return check_role