"""Reporting routes for managers and owners."""

from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials

from auth import get_optional_user, require_role, security
from models import InventoryReport, SalesReport, TopSellingItem

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/inventory", response_model=InventoryReport)
async def get_inventory_report(
    request: Request,
    category: Optional[str] = None,
    material: Optional[str] = None,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Get inventory report. Requires manager+ role."""
    db = request.app.state.db

    # Authenticate and check role
    user = await get_optional_user(request, credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Authorization required")
    require_role("manager")(user)

    # Build query
    query = {}
    if category:
        query["category"] = category
    if material:
        query["material"] = material

    # Get all items
    items = await db.jewellery_items.find(query).to_list(length=10000)

    # Calculate statistics
    total_items = len(items)
    available_items = sum(1 for item in items if item["status"] == "available")
    sold_items = sum(1 for item in items if item["status"] == "sold")
    reserved_items = sum(1 for item in items if item["status"] == "reserved")
    total_value = sum(item["price"] for item in items)

    # Group by category
    by_category = {}
    for item in items:
        cat = item["category"]
        by_category[cat] = by_category.get(cat, 0) + 1

    # Group by material
    by_material = {}
    for item in items:
        mat = item["material"]
        by_material[mat] = by_material.get(mat, 0) + 1

    return InventoryReport(
        total_items=total_items,
        available_items=available_items,
        sold_items=sold_items,
        reserved_items=reserved_items,
        total_value=total_value,
        by_category=by_category,
        by_material=by_material,
    )


@router.get("/sales", response_model=SalesReport)
async def get_sales_report(
    request: Request,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Get sales report. Requires manager+ role."""
    db = request.app.state.db

    # Authenticate and check role
    user = await get_optional_user(request, credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Authorization required")
    require_role("manager")(user)

    # Parse dates or use defaults (last 30 days)
    if end_date:
        end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
    else:
        end_dt = datetime.now(timezone.utc)

    if start_date:
        start_dt = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
    else:
        start_dt = end_dt - timedelta(days=30)

    # Validate date range
    if end_dt < start_dt:
        raise HTTPException(
            status_code=400,
            detail="end_date must be after start_date",
        )

    if (end_dt - start_dt).days > 365:
        raise HTTPException(
            status_code=400,
            detail="Date range cannot exceed 1 year",
        )

    # Build query
    query = {
        "order_date": {
            "$gte": start_dt,
            "$lte": end_dt,
        }
    }

    # Get orders in date range
    orders = await db.orders.find(query).to_list(length=10000)

    total_orders = len(orders)
    completed_orders = sum(1 for order in orders if order["status"] == "delivered")
    pending_orders = sum(
        1
        for order in orders
        if order["status"] in ["pending", "confirmed"]
    )
    total_revenue = sum(
        order["total_amount"]
        for order in orders
        if order["status"] == "delivered"
    )

    # Calculate top selling items
    item_sales = {}
    for order in orders:
        if order["status"] == "delivered":
            for item in order["items"]:
                key = item["item_code"]
                if key not in item_sales:
                    item_sales[key] = {
                        "item_code": item["item_code"],
                        "name": item["name"],
                        "quantity": 0,
                    }
                item_sales[key]["quantity"] += item["quantity"]

    # Sort by quantity and get top 10
    top_items = sorted(
        item_sales.values(),
        key=lambda x: x["quantity"],
        reverse=True,
    )[:10]

    return SalesReport(
        total_orders=total_orders,
        completed_orders=completed_orders,
        pending_orders=pending_orders,
        total_revenue=total_revenue,
        date_range={
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
        },
        top_selling_items=[TopSellingItem(**item) for item in top_items],
    )