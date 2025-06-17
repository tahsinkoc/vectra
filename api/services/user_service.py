from api.schemas.user import UserCreate
from api.db.mongo import db
from bcrypt import hashpw, gensalt, checkpw

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
        "hashed_password": hashed_pw
    }
    result = db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id), "name": user.name, "surname": user.surname, "email": user.email}

async def get_all_users():
    return list(db.users.find({}, {"_id": 0}))
