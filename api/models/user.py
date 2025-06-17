from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    id: Optional[str]
    name: str
    surname: str
    email: str
    password: str
