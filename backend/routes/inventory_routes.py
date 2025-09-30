"""Inventory management routes."""

from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from auth import get_optional_user, require_role, security
from models import (
    JewelleryItem,
    JewelleryItemCreate,
    JewelleryItemsResponse,
    JewelleryItemUpdate,
    User,
)

router = APIRouter(prefix="/inventory", tags=["inventory"])

# Optional security dependency that doesn't raise exceptions
optional_security = HTTPBearer(auto_error=False)


@router.get("/items", response_model=JewelleryItemsResponse)
async def get_items(
    request: Request,
    page: int = 1,
    limit: int = 20,
    category: Optional[str] = None,
    material: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(optional_security),
):
    """
    Get jewellery items.
    Public users only see available items.
    Authenticated users see all items.
    """
    db = request.app.state.db

    # Get current user if authenticated
    user = await get_optional_user(request, credentials)

    # Build query
    query = {}

    # Public users can only see available items
    if user is None:
        query["status"] = "available"
    elif status:
        query["status"] = status

    if category:
        query["category"] = category
    if material:
        query["material"] = material
    if search:
        query["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
            {"item_code": {"$regex": search, "$options": "i"}},
        ]

    # Pagination
    limit = min(limit, 100)
    skip = (page - 1) * limit

    # Execute query
    items_cursor = db.jewellery_items.find(query).skip(skip).limit(limit + 1)
    items_list = await items_cursor.to_list(length=limit + 1)

    has_more = len(items_list) > limit
    items_list = items_list[:limit]

    total = await db.jewellery_items.count_documents(query)

    items = [
        JewelleryItem(
            id=item["_id"],
            item_code=item["item_code"],
            name=item["name"],
            description=item["description"],
            category=item["category"],
            price=item["price"],
            weight=item["weight"],
            material=item["material"],
            images=item.get("images", []),
            status=item["status"],
            created_at=item["created_at"],
            updated_at=item["updated_at"],
        )
        for item in items_list
    ]

    return JewelleryItemsResponse(
        items=items,
        page=page,
        total=total,
        has_more=has_more,
    )


@router.post("/items", response_model=JewelleryItem, status_code=201)
async def create_item(
    item_data: JewelleryItemCreate,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Create a new jewellery item. Requires staff+ role."""
    try:
        db = request.app.state.db

        # Authenticate and check role
        user = await get_optional_user(request, credentials)
        if not user:
            raise HTTPException(status_code=401, detail="Authorization required")
        require_role("staff")(user)
    except HTTPException:
        raise
    except Exception as e:
        import logging
        logging.error(f"Error in auth: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

    try:
        # Check if item_code already exists
        existing = await db.jewellery_items.find_one({"item_code": item_data.item_code})
        if existing:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "ITEM_CODE_EXISTS", "message": "Item code already exists"}},
            )

        # Create item
        item = JewelleryItem(
            item_code=item_data.item_code,
            name=item_data.name,
            description=item_data.description,
            category=item_data.category,
            price=item_data.price,
            weight=item_data.weight,
            material=item_data.material,
            images=item_data.images or [],
        )

        # Convert to dict and use _id instead of id for MongoDB
        item_dict = item.model_dump()
        item_dict["_id"] = item_dict.pop("id")
        await db.jewellery_items.insert_one(item_dict)

        return item
    except HTTPException:
        raise
    except Exception as e:
        import logging
        logging.error(f"Error creating item: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/items/{item_id}", response_model=JewelleryItem)
async def update_item(
    item_id: str,
    update_data: JewelleryItemUpdate,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Update a jewellery item. Requires staff+ role."""
    db = request.app.state.db

    # Authenticate and check role
    user = await get_optional_user(request, credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Authorization required")
    require_role("staff")(user)

    # Check if item exists
    existing = await db.jewellery_items.find_one({"_id": item_id})
    if not existing:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "ITEM_NOT_FOUND", "message": "Item not found"}},
        )

    # Check if new item_code conflicts with another item
    if update_data.item_code and update_data.item_code != existing["item_code"]:
        code_exists = await db.jewellery_items.find_one(
            {"item_code": update_data.item_code, "_id": {"$ne": item_id}}
        )
        if code_exists:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "ITEM_CODE_EXISTS", "message": "Item code already exists"}},
            )

    # Build update dict (only include provided fields)
    update_dict = update_data.model_dump(exclude_unset=True)
    if update_dict:
        update_dict["updated_at"] = datetime.now(timezone.utc)

        await db.jewellery_items.update_one({"_id": item_id}, {"$set": update_dict})

    # Fetch and return updated item
    updated_item = await db.jewellery_items.find_one({"_id": item_id})

    return JewelleryItem(
        id=updated_item["_id"],
        item_code=updated_item["item_code"],
        name=updated_item["name"],
        description=updated_item["description"],
        category=updated_item["category"],
        price=updated_item["price"],
        weight=updated_item["weight"],
        material=updated_item["material"],
        images=updated_item.get("images", []),
        status=updated_item["status"],
        created_at=updated_item["created_at"],
        updated_at=updated_item["updated_at"],
    )