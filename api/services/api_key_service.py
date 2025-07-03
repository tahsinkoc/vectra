from api.models.api_key import ApiKeyModel as ApiKey
from api.schemas.api_key import ApiKeyRegister, ApiKeyResponse, ApıKeyDelete
from api.db.mongo import db
from fastapi import HTTPException
import datetime as dt
import secrets

def create_api_key(api_key_data: ApiKeyRegister, email:str) -> ApiKeyResponse:
    print(email)
    if email is None or email == "":
        raise ValueError("Email must be provided")
    else:
        res = db.users.find_one({"email": email})
        if res is None:
            raise ValueError("User not found with the provided email")
        else:

            if db.apiKeys.find_one({"user_id": res["_id"]}):
                raise ValueError("User already has an API key")
            else:
                key = secrets.token_hex(16)

                api_key:ApiKey = {
                    "name": api_key_data["name"],
                    "key": key,
                    "user_id": res["_id"],
                    "created_at": dt.datetime.now(),
                    "updated_at": None
                } 
                
                db.apiKeys.insert_one(api_key)

                inserted = db.apiKeys.find_one({"key": key})

                return ApiKeyResponse(
                    id=str(inserted["_id"]),
                    name=inserted["name"],
                    key=inserted["key"],
                    created_at=inserted["created_at"].isoformat(),
                    updated_at=inserted["updated_at"].isoformat() if inserted["updated_at"] else None,
                )
            
def confirm_api_key(key:str):
    if (key is None or key == ""):
        raise HTTPException(status_code=401, detail="API KEY DOESN`T PROVIDED")
    else:
        res = db.apiKeys.find_one({"key": key})
        if res is None:
            raise HTTPException(status_code=401, detail="THE PROVIDED API KEY NOT VALID")
        else:
            return True