from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.menu import MenuItem, FoodCategory
from app.models.user import User
from app.schemas.menu import (
    MenuItemCreate,
    MenuItemUpdate,
    MenuItemResponse,
)
from app.core.dependencies import get_current_user, require_admin


router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


# =========================
# GET MENU
# Customer + Admin
# =========================

@router.get("/", response_model=list[MenuItemResponse])
def get_menu(
    search: Optional[str] = Query(None),
    category: Optional[FoodCategory] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(MenuItem)

    # Search by name
    if search:
        query = query.filter(
            MenuItem.name.ilike(f"%{search}%")
        )

    # Filter by category
    if category:
        query = query.filter(
            MenuItem.category == category
        )

    return query.all()


# =========================
# CREATE MENU ITEM
# Admin only
# =========================

@router.post(
    "/",
    response_model=MenuItemResponse,
    status_code=201
)
def create_menu_item(
    data: MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    menu_item = MenuItem(
        name=data.name,
        category=data.category,
        price=data.price,
        description=data.description,
        image_url=data.image_url,
        is_available=data.is_available,
    )

    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)

    return menu_item


# =========================
# UPDATE MENU ITEM
# Admin only
# =========================

@router.put(
    "/{menu_id}",
    response_model=MenuItemResponse
)
def update_menu_item(
    menu_id: int,
    data: MenuItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    menu_item = (
        db.query(MenuItem)
        .filter(MenuItem.id == menu_id)
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )

    update_data = data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(menu_item, key, value)

    db.commit()
    db.refresh(menu_item)

    return menu_item


# =========================
# DELETE MENU ITEM
# Admin only
# =========================

@router.delete("/{menu_id}")
def delete_menu_item(
    menu_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    menu_item = (
        db.query(MenuItem)
        .filter(MenuItem.id == menu_id)
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )

    db.delete(menu_item)
    db.commit()

    return {
        "message": "Menu item deleted successfully"
    }