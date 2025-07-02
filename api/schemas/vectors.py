from pydantic import BaseModel
from typing import List

class CreateVector(BaseModel):
    id: str
    metadata: str
    name: str
    numericId: int

class SearchVector(BaseModel):
    metadata: str

class CreateVectorResponse(BaseModel):
    id: str