from fastapi import APIRouter, Depends, HTTPException, Request
from api.schemas.vectors import CreateVector
from api.services.vector_service import create_vector
from api.models.vector import Vector

router = APIRouter()

@router.post("/")
async def create_vector_route(vector: CreateVector, Request: Request):
    result = await create_vector(vector, Request)
    return result
    
