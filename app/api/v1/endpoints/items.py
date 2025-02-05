from fastapi import APIRouter
from app.schemas.item import Item

router = APIRouter()

@router.get("/", response_model=list[Item])
def get_items():
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
