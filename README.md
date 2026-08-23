py -3.11 -m venv venv
venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-dotenv pydantic-settings python-jose[cryptography] passlib[bcrypt] python-multipart

pip freeze > requirements.txt