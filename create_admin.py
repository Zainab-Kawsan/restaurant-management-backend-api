from app.database import SessionLocal
from app.models.user import User, UserRole
from app.core.security import hash_password


db = SessionLocal()

admin = User(
    name="mahdi",
    email="mahdi@gmail.com",
    password=hash_password("admin123"),
    role=UserRole.ADMIN
)

db.add(admin)
db.commit()
db.refresh(admin)

print("Admin created:", admin.email)

db.close()