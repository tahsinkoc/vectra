from fastapi import APIRouter, HTTPException
from api.schemas.user import UserCreate, UserLogin
from api.services.user_service import create_user, get_all_users, login_user

router = APIRouter()

@router.post("/")
async def create(user: UserCreate):
    return await create_user(user)

@router.post("/login")
async def login(user: UserLogin):
    try:
        return await login_user (user)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get("/")
async def list_users():
    return await get_all_users()
