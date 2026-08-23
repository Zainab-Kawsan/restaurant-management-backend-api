from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, Text
from sqlalchemy.orm import relationship
import enum

from app.database import Base


class FoodCategory(str, enum.Enum):
    STARTER = "starter"
    MAIN_COURSE = "main_course"
    DESSERT = "dessert"
    DRINKS = "drinks"


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(255),
        nullable=False,
        index=True
    )

    category = Column(
        Enum(FoodCategory),
        nullable=False,
        index=True
    )

    price = Column(
        Float,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    image_url = Column(
        String(500),
        nullable=True
    )

    is_available = Column(
        Boolean,
        default=True,
        nullable=False
    )

    order_items = relationship(
        "OrderItem",
        back_populates="food"
    )