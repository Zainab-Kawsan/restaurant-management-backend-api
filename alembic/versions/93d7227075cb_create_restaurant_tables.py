"""create restaurant tables

Revision ID: 93d7227075cb
Revises:
Create Date: 2026-08-22 13:25:52.192381
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "93d7227075cb"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =========================
    # USERS
    # =========================

    op.create_table(
        "users",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "name",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "password",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "role",
            sa.Enum(
                "ADMIN",
                "CUSTOMER",
                name="userrole"
            ),
            nullable=False
        ),
    )

    op.create_index(
        "ix_users_id",
        "users",
        ["id"]
    )

    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True
    )


    # =========================
    # MENU ITEMS
    # =========================

    op.create_table(
        "menu_items",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "name",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "category",
            sa.Enum(
                "STARTER",
                "MAIN_COURSE",
                "DESSERT",
                "DRINKS",
                name="foodcategory"
            ),
            nullable=False
        ),

        sa.Column(
            "price",
            sa.Float(),
            nullable=False
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            "image_url",
            sa.String(length=500),
            nullable=True
        ),

        sa.Column(
            "is_available",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true()
        ),
    )

    op.create_index(
        "ix_menu_items_id",
        "menu_items",
        ["id"]
    )

    op.create_index(
        "ix_menu_items_name",
        "menu_items",
        ["name"]
    )

    op.create_index(
        "ix_menu_items_category",
        "menu_items",
        ["category"]
    )


    # =========================
    # ORDERS
    # =========================

    op.create_table(
        "orders",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "total_price",
            sa.Float(),
            nullable=False
        ),

        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "PREPARING",
                "OUT_FOR_DELIVERY",
                "DELIVERED",
                name="orderstatus"
            ),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"]
        ),
    )

    op.create_index(
        "ix_orders_id",
        "orders",
        ["id"]
    )


    # =========================
    # ORDER ITEMS
    # =========================

    op.create_table(
        "order_items",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "order_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "food_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "quantity",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "unit_price",
            sa.Float(),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["order_id"],
            ["orders.id"]
        ),

        sa.ForeignKeyConstraint(
            ["food_id"],
            ["menu_items.id"]
        ),
    )

    op.create_index(
        "ix_order_items_id",
        "order_items",
        ["id"]
    )


def downgrade() -> None:

    op.drop_table("order_items")
    op.drop_table("orders")
    op.drop_table("menu_items")
    op.drop_table("users")