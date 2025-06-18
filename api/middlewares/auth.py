# from fastapi import Request, HTTPException

# async def api_key_middleware(request: Request, call_next):
#     api_key = request.headers.get("X-API-Key")
#     if api_key != "your-secret-key":
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return await call_next(request)

from fastapi import Request, HTTPException
from api.helper.token_handler import confirm_token

#Bearer authentication middleware
async def bearer_auth_middleware(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return False
    
    token = auth_header.split(" ")[1]
    try:
        # Verify the token
        
        a = confirm_token(token)
        if not a:
            return {"status": False, "message": "Invalid or expired token"}
        else:
            return {"status": True, "message": "Token is valid", "email": a.email}
    except Exception as e:
        return {"status": False, "message": str(e)}
    
    # return await call_next(request)