from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.models.order import OrderStatus


class OrderItemCreate(BaseModel):
    food_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    food_id: int
    quantity: int
    unit_price: float

    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: OrderStatus
    created_at: datetime
    order_items: list[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)


class OrderStatusUpdate(BaseModel):
    status: OrderStatus