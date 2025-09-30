"""Authentication routes."""

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials

from auth import create_access_token, get_current_user, security, verify_password
from models import LoginRequest, LoginResponse, User

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest, request: Request):
    """Authenticate user and return JWT token."""
    db = request.app.state.db

    user_data = await db.users.find_one({"email": login_data.email})
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(login_data.password, user_data["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = User(
        id=user_data["_id"],
        username=user_data["username"],
        email=user_data["email"],
        role=user_data["role"],
        created_at=user_data["created_at"],
    )

    token = create_access_token(user)

    return LoginResponse(token=token, user=user)


@router.get("/me", response_model=User)
async def get_me(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Get current authenticated user."""
    return await get_current_user(request, credentials)