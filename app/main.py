from fastapi import FastAPI

from app.routers.auth import router as auth_router

from app.routers.menu import router as menu_router

from app.routers.order import router as order_router

app = FastAPI(
    title="Restaurant Management API",
    description="Backend API for restaurant menu and order management",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(menu_router)
app.include_router(order_router)

@app.get("/")
def root():
    return {
        "message": "Restaurant Management API is running"
    }