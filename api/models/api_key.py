from pydantic import BaseModel
from typing import Optional

class ApiKeyModel(BaseModel):
    id: Optional[str] = None
    user_id: str
    name: str
    key: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None