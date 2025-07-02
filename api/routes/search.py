from fastapi import APIRouter
from api.schemas.vectors import SearchVector
from api.services.search_service import search_vector

router = APIRouter()

@router.post("/")
async def search(vector: SearchVector):
    return await search_vector(vector)
