from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order, OrderStatus
from app.models.order_item import OrderItem
from app.models.menu import MenuItem
from app.models.user import User

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderStatusUpdate,
)

from app.core.dependencies import (
    get_current_user,
    require_admin,
)


router = APIRouter(
    prefix="/order",
    tags=["Orders"]
)

@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201
)
@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201
)
def create_order(
    data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not data.items:
        raise HTTPException(
            status_code=400,
            detail="Order must contain at least one item"
        )

    total_price = 0
    validated_items = []

    # Validate food items and calculate total
    for item in data.items:

        if item.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than 0"
            )

        food = (
            db.query(MenuItem)
            .filter(MenuItem.id == item.food_id)
            .first()
        )

        if not food:
            raise HTTPException(
                status_code=404,
                detail=f"Food item {item.food_id} not found"
            )

        if not food.is_available:
            raise HTTPException(
                status_code=400,
                detail=f"{food.name} is not available"
            )

        item_total = food.price * item.quantity
        total_price += item_total

        validated_items.append({
            "food_id": food.id,
            "quantity": item.quantity,
            "unit_price": food.price
        })

    # Create order
    order = Order(
        user_id=current_user.id,
        total_price=total_price,
        status=OrderStatus.PENDING
    )

    db.add(order)
    db.flush()

    # Create order items
    for item in validated_items:

        order_item = OrderItem(
            order_id=order.id,
            food_id=item["food_id"],
            quantity=item["quantity"],
            unit_price=item["unit_price"]
        )

        db.add(order_item)

    db.commit()
    db.refresh(order)

    return order

@router.get(
    "/my-orders",
    response_model=list[OrderResponse]
)
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Order)
        .filter(Order.user_id == current_user.id)
        .order_by(Order.created_at.desc())
        .all()
    )
    
@router.get(
    "/all",
    response_model=list[OrderResponse]
)
def get_all_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return (
        db.query(Order)
        .order_by(Order.created_at.desc())
        .all()
    )
@router.put(
    "/{order_id}/status",
    response_model=OrderResponse
)
def update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.status = data.status

    db.commit()
    db.refresh(order)

    return order