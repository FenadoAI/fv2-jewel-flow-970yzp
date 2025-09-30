"""Order management routes."""

from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials

from auth import get_optional_user, require_role, security
from models import (
    JewelleryItem,
    Order,
    OrderCreate,
    OrderItem,
    OrdersResponse,
    OrderStatusUpdate,
)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=Order, status_code=201)
async def create_order(order_data: OrderCreate, request: Request):
    """
    Place a COD order.
    Public endpoint - no authentication required.
    """
    db = request.app.state.db

    # Validate all items exist and are available
    order_items = []
    total_amount = 0

    for item_req in order_data.items:
        item = await db.jewellery_items.find_one({"_id": item_req.item_id})

        if not item:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": {
                        "code": "ITEM_NOT_FOUND",
                        "message": f"Item {item_req.item_id} not found",
                    }
                },
            )

        if item["status"] != "available":
            raise HTTPException(
                status_code=400,
                detail={
                    "error": {
                        "code": "ITEM_UNAVAILABLE",
                        "message": f"Item {item['item_code']} is not available",
                    }
                },
            )

        subtotal = item["price"] * item_req.quantity
        total_amount += subtotal

        order_items.append(
            OrderItem(
                item_id=item["_id"],
                item_code=item["item_code"],
                name=item["name"],
                price=item["price"],
                quantity=item_req.quantity,
                subtotal=subtotal,
            )
        )

    # Create order
    order = Order(
        customer_name=order_data.customer_name,
        customer_phone=order_data.customer_phone,
        customer_address=order_data.customer_address,
        items=order_items,
        total_amount=total_amount,
    )

    # Convert to dict and use _id instead of id for MongoDB
    order_dict = order.model_dump()
    order_dict["_id"] = order_dict.pop("id")
    order_dict["items"] = [item.model_dump() for item in order_items]
    await db.orders.insert_one(order_dict)

    return order


@router.get("", response_model=OrdersResponse)
async def get_orders(
    request: Request,
    page: int = 1,
    limit: int = 20,
    status: Optional[str] = None,
    customer_phone: Optional[str] = None,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Get orders. Requires staff+ role."""
    db = request.app.state.db

    # Authenticate and check role
    user = await get_optional_user(request, credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Authorization required")
    require_role("staff")(user)

    # Build query
    query = {}
    if status:
        query["status"] = status
    if customer_phone:
        query["customer_phone"] = customer_phone

    # Pagination
    limit = min(limit, 100)
    skip = (page - 1) * limit

    # Execute query - sorted by order_date descending
    orders_cursor = (
        db.orders.find(query).sort("order_date", -1).skip(skip).limit(limit)
    )
    orders_list = await orders_cursor.to_list(length=limit)

    total = await db.orders.count_documents(query)

    orders = [
        Order(
            id=order["_id"],
            customer_name=order["customer_name"],
            customer_phone=order["customer_phone"],
            customer_address=order["customer_address"],
            items=[OrderItem(**item) for item in order["items"]],
            total_amount=order["total_amount"],
            status=order["status"],
            payment_method=order["payment_method"],
            order_date=order["order_date"],
            delivery_date=order.get("delivery_date"),
        )
        for order in orders_list
    ]

    return OrdersResponse(orders=orders, page=page, total=total)


@router.patch("/{order_id}/status", response_model=Order)
async def update_order_status(
    order_id: str,
    status_data: OrderStatusUpdate,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Update order status. Requires staff+ role."""
    db = request.app.state.db

    # Authenticate and check role
    user = await get_optional_user(request, credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Authorization required")
    require_role("staff")(user)

    # Check if order exists
    existing = await db.orders.find_one({"_id": order_id})
    if not existing:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "ORDER_NOT_FOUND", "message": "Order not found"}},
        )

    # Build update dict
    update_dict = {"status": status_data.status}

    # Set delivery_date if status is delivered and date provided
    if status_data.status == "delivered":
        update_dict["delivery_date"] = (
            status_data.delivery_date or datetime.now(timezone.utc)
        )

    await db.orders.update_one({"_id": order_id}, {"$set": update_dict})

    # Fetch and return updated order
    updated_order = await db.orders.find_one({"_id": order_id})

    return Order(
        id=updated_order["_id"],
        customer_name=updated_order["customer_name"],
        customer_phone=updated_order["customer_phone"],
        customer_address=updated_order["customer_address"],
        items=[OrderItem(**item) for item in updated_order["items"]],
        total_amount=updated_order["total_amount"],
        status=updated_order["status"],
        payment_method=updated_order["payment_method"],
        order_date=updated_order["order_date"],
        delivery_date=updated_order.get("delivery_date"),
    )