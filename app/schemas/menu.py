from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.menu import FoodCategory


class MenuItemCreate(BaseModel):
    name: str
    category: FoodCategory
    price: float
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_available: bool = True


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[FoodCategory] = None
    price: Optional[float] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_available: Optional[bool] = None


class MenuItemResponse(BaseModel):
    id: int
    name: str
    category: FoodCategory
    price: float
    description: Optional[str]
    image_url: Optional[str]
    is_available: bool

    model_config = ConfigDict(from_attributes=True)