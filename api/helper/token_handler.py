import jwt
from datetime import datetime, timedelta, timezone
from api.schemas.user import UserForToken
from api.config import JWT_SECRET_KEY

secret_key = JWT_SECRET_KEY

def create_token(user: UserForToken, algorithm: str = "HS256", expires_in: int = 3600) -> str:
    expiration = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    user.update({"exp": expiration})
    return jwt.encode(user, secret_key, algorithm=algorithm)

def confirm_token(token: str, algorithm: str = "HS256") -> UserForToken:
    try:
        decoded = jwt.decode(token, secret_key, algorithms=[algorithm])
        return UserForToken(**decoded)
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
    except Exception as e:
        raise ValueError(f"An error occurred while decoding the token: {str(e)}")