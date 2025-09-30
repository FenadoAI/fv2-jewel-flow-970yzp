"""Pydantic models for jewellery store management system."""

import uuid
from datetime import datetime, timezone
from typing import List, Literal, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


# User models
UserRole = Literal["staff", "manager", "owner"]


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: EmailStr
    role: UserRole
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class UserInDB(User):
    password_hash: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    user: User


# Jewellery Item models
ItemStatus = Literal["available", "sold", "reserved"]


class JewelleryItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    item_code: str
    name: str
    description: str
    category: str
    price: int  # cents
    weight: float  # grams
    material: str
    images: List[str] = Field(default_factory=list)
    status: ItemStatus = "available"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("item_code")
    @classmethod
    def validate_item_code(cls, v: str) -> str:
        if not v or len(v) > 50:
            raise ValueError("item_code must be 1-50 characters")
        # Allow alphanumeric plus _, -, and .
        if not v.replace("_", "").replace("-", "").replace(".", "").isalnum():
            raise ValueError("item_code must be alphanumeric (with _, -, or .)")
        return v

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 3 or len(v) > 200:
            raise ValueError("name must be 3-200 characters")
        return v

    @field_validator("price")
    @classmethod
    def validate_price(cls, v: int) -> int:
        if v < 0:
            raise ValueError("price must be >= 0")
        return v

    @field_validator("weight")
    @classmethod
    def validate_weight(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("weight must be > 0")
        return v


class JewelleryItemCreate(BaseModel):
    item_code: str
    name: str
    description: str
    category: str
    price: int
    weight: float
    material: str
    images: Optional[List[str]] = None


class JewelleryItemUpdate(BaseModel):
    item_code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[int] = None
    weight: Optional[float] = None
    material: Optional[str] = None
    images: Optional[List[str]] = None
    status: Optional[ItemStatus] = None


class JewelleryItemsResponse(BaseModel):
    items: List[JewelleryItem]
    page: int
    total: int
    has_more: bool


# Order models
OrderStatus = Literal["pending", "confirmed", "delivered", "cancelled"]


class OrderItem(BaseModel):
    item_id: str
    item_code: str
    name: str
    price: int
    quantity: int
    subtotal: int


class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    customer_name: str
    customer_phone: str
    customer_address: str
    items: List[OrderItem]
    total_amount: int
    status: OrderStatus = "pending"
    payment_method: Literal["COD"] = "COD"
    order_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    delivery_date: Optional[datetime] = None

    @field_validator("customer_name")
    @classmethod
    def validate_customer_name(cls, v: str) -> str:
        if len(v) < 2 or len(v) > 100:
            raise ValueError("customer_name must be 2-100 characters")
        return v

    @field_validator("customer_address")
    @classmethod
    def validate_customer_address(cls, v: str) -> str:
        if len(v) < 10:
            raise ValueError("customer_address must be at least 10 characters")
        return v

    @field_validator("items")
    @classmethod
    def validate_items(cls, v: List[OrderItem]) -> List[OrderItem]:
        if not v:
            raise ValueError("items cannot be empty")
        return v


class OrderCreateItem(BaseModel):
    item_id: str
    quantity: int

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("quantity must be > 0")
        return v


class OrderCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_address: str
    items: List[OrderCreateItem]


class OrderStatusUpdate(BaseModel):
    status: OrderStatus
    delivery_date: Optional[datetime] = None


class OrdersResponse(BaseModel):
    orders: List[Order]
    page: int
    total: int


# Report models
class InventoryReport(BaseModel):
    total_items: int
    available_items: int
    sold_items: int
    reserved_items: int
    total_value: int  # cents
    by_category: dict[str, int]
    by_material: dict[str, int]


class TopSellingItem(BaseModel):
    item_code: str
    name: str
    quantity: int


class SalesReport(BaseModel):
    total_orders: int
    completed_orders: int
    pending_orders: int
    total_revenue: int  # cents
    date_range: dict[str, str]
    top_selling_items: List[TopSellingItem]


# Error model
class ErrorResponse(BaseModel):
    error: dict[str, str]