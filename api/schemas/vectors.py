from pydantic import BaseModel
from typing import List

class CreateVector(BaseModel):
    id: str
    metadata: str
    name: str
    
class CreateVectorResponse(BaseModel):
    id: str