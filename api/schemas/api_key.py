from pydantic import BaseModel
from typing import Optional

class ApiKeyRegister(BaseModel):
    name: str

class ApiKeyResponse(BaseModel):
    id: str
    name: str
    key: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ApıKeyDelete(BaseModel):
    id: str
    name: str