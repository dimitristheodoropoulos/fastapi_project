from app.db.session import SessionLocal
from app.models.user import User as DBUser

def get_users(db: SessionLocal):
    return db.query(DBUser).all()
