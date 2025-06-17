from api.models.api_key import ApiKeyModel as ApiKey
from api.schemas.api_key import ApiKeyRegister, ApiKeyResponse, ApıKeyDelete
from api.db.mongo import db
import datetime as dt
import secrets

def create_api_key(api_key_data: ApiKeyRegister) -> ApiKeyResponse:

    key = secrets.token_hex(16)

    api_key:ApiKey = {
        "name": api_key_data["name"],
        "key": key,
        "created_at": dt.datetime.now(),
        "updated_at": None
    } 
    
    db.apiKeys.insert_one(api_key)

    # Fetch the inserted document to get the generated _id and correct types
    inserted = db.apiKeys.find_one({"key": key})

    return ApiKeyResponse(
        id=str(inserted["_id"]),
        name=inserted["name"],
        key=inserted["key"],
        created_at=inserted["created_at"].isoformat(),
        updated_at=inserted["updated_at"].isoformat() if inserted["updated_at"] else None,
    )