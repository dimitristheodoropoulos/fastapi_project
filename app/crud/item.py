#from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.models.item import Item as DBItem

""" def get_items(db: SessionLocal):
    return db.query(DBItem).all() """


def get_items(db: Session):
    return db.query(DBItem).all()