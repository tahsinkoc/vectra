from fastapi import FastAPI
from api.routes import user, api_key
# from api.middlewares.auth import api_key_middleware

app = FastAPI()

# app.middleware("http")(api_key_middleware)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(api_key.router, prefix="/api-key", tags=["API Keys"])