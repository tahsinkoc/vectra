from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    surname: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    name: str
    surname: str
    email: str

    class Config:
        orm_mode = True
