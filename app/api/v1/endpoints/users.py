from fastapi import APIRouter
from app.schemas.user import User

router = APIRouter()

@router.get("/", response_model=list[User])
def get_users():
    return [{"id": 1, "name": "User 1"}, {"id": 2, "name": "User 2"}]
