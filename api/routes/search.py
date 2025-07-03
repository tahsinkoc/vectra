from fastapi import APIRouter, Request
from api.schemas.vectors import SearchVector
from api.services.search_service import search_vector, search_vector_response_with_id

router = APIRouter()

@router.post("/")
async def search(vector: SearchVector, Request: Request):
    return await search_vector(vector, Request)

@router.post("/sm/ids")
async def search_small(vector: SearchVector, Request: Request):
    return await search_vector_response_with_id(vector, Request)