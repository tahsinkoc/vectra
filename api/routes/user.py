from fastapi import APIRouter, HTTPException
from api.schemas.user import UserCreate
from api.services.user_service import create_user, get_all_users

router = APIRouter()

@router.post("/")
async def create(user: UserCreate):
    return await create_user(user)

@router.get("/")
async def list_users():
    return await get_all_users()
