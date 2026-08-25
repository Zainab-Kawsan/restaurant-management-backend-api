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
```

Admin

Admins can:
```text
POST /menu
PUT /menu/{id}
DELETE /menu/{id}
GET /orders
PUT /order/{id}/status
```


Admin-only endpoints are protected using role-based authorization.



## Deployment

### 1. Create Online MySQL Database

We used **Aiven MySQL** as the cloud database so the deployed FastAPI application can access the database online.

The database connection uses:

```env
DATABASE_URL=mysql+pymysql://USER:PASSWORD@HOST:PORT/defaultdb
````

### 2. Configure Environment Variables

The application reads the database and security settings from environment variables:

```env
DATABASE_URL=...
SECRET_KEY=...
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

The `.env` file is not uploaded to GitHub.

### 3. Run Database Migrations

After connecting the project to the online database:

```bash
alembic upgrade head
```

This creates the required tables

### 4. Push Project to GitHub

```bash
git add .
git commit -m "Prepare project for deployment"
git push origin main
```

### 5. Create Render Web Service

On Render:

```text
New → Web Service
```

Connect the GitHub repository and select the `main` branch.

### 6. Configure Render

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### 7. Add Environment Variables

In Render → Environment Variables, add:

```text
DATABASE_URL
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
```

### 8. Deploy

Click **Deploy Web Service**.

Render will:

```text
GitHub
   ↓
Install dependencies
   ↓
Start FastAPI
   ↓
Connect to Aiven MySQL
   ↓
Application online
```

### 9. Access the API

After deployment, Render provides a public URL:

Swagger documentation:

```text
https://restaurant-management-backend-api-adv7.onrender.com/docs
```



