# from fastapi import Request, HTTPException

# async def api_key_middleware(request: Request, call_next):
#     api_key = request.headers.get("X-API-Key")
#     if api_key != "your-secret-key":
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return await call_next(request)
