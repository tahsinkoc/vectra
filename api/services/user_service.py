from fastapi import HTTPException
from api.schemas.user import UserCreate, UserLogin
from api.db.mongo import db
from bcrypt import hashpw, gensalt, checkpw
from api.helper.token_handler import create_token

async def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


async def create_user(user: UserCreate):
    hashed_pw = await hash_password(user.password)
    user_dict = {
        "name": user.name,
        "surname": user.surname,
        "email": user.email,
        "password": hashed_pw
    }
    result = db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id), "name": user.name, "surname": user.surname, "email": user.email}

async def login_user(usera: UserLogin):
    print("Login attempt for user:", usera.email)
    user = db.users.find_one({"email": usera.email}, {"_id": 0})
    if user and await verify_password(usera.password, user['password']):
        print("name", user)
        return {"message": "Login successful", "token": create_token(user)}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    

async def get_all_users():
    return list(db.users.find({}, {"_id": 0}))
