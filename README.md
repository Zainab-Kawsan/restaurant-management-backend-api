#  Restaurant Management Backend API

A RESTful backend API for managing restaurant menu items, customers, 
orders, and order tracking.

## 🚀 Features

### Authentication
- User signup and login
- JWT authentication
- Role-based authorization
- Customer and Admin roles

### Menu Management
- Create food items
- Update food items
- Delete food items
- View menu
- Search food items
- Filter by category
- Availability management

### Order Management
- Place orders
- Calculate order total
- View order history
- View order status
- Admin order management
- Update order status

## 🛠️ Technologies

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- JWT
- Pydantic
- Passlib / bcrypt
- Swagger / OpenAPI

## 🗄️ Database

The application uses MySQL with the following tables:

- users
- menu_items
- orders
- order_items

## 🔐 Authentication

The API uses JWT Bearer Authentication.

The authentication flow is:

Signup
   ↓
User Account
   ↓
Login
   ↓
JWT Access Token
   ↓
Authorize Protected Endpoints

Passwords are hashed before being stored in the database.

Passwords are never returned in API responses.


## 📡 API Endpoints

### Authentication

POST `/auth/signup`

POST `/auth/login`

### Menu

GET `/menu`

POST `/menu`

PUT `/menu/{id}`

DELETE `/menu/{id}`

### Orders

POST `/order`

GET `/order/my-orders`

GET `/order`

PUT `/order/{id}/status`

## ▶ Run the Project

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:
```bash
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
alembic upgrade head
```

Start the server:
```bash
uvicorn app.main:app --reload
```

📚 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

<img width="960" height="509" alt="rest-swagger" src="https://github.com/user-attachments/assets/31ff73a6-d5a4-48e4-973c-deeea46f6ccc" />


## 👥 User Roles

The system supports two roles:

Customer

Customers can:
```text
GET /menu
POST /order
GET /my-orders
Admin

Admins can:

POST /menu
PUT /menu/{id}
DELETE /menu/{id}
GET /orders
PUT /order/{id}/status

Admin-only endpoints are protected using role-based authorization.





