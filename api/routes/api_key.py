from fastapi import APIRouter, HTTPException, Depends, Request
from api.schemas.api_key import ApiKeyResponse, ApiKeyRegister
from api.services.api_key_service import create_api_key
from api.middlewares.auth import bearer_auth_middleware

router = APIRouter()

@router.post("/", response_model=ApiKeyResponse)
async def create(api_key_data: ApiKeyRegister, request: Request):
    print(api_key_data)
    result = await bearer_auth_middleware(request)
    if (result["status"] != True):
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        try:
            return create_api_key({"name": api_key_data.name}, result.get("email"))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



# @router.delete("/{api_key_id}", response_model=dict)
# async def delete(api_key_id: str):
#     try:
#         result = await delete_api_key(api_key_id)
#         if result:
#             return {"message": "API key deleted successfully"}
#         else:
#             raise HTTPException(status_code=404, detail="API key not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))