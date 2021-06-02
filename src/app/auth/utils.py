# JWT
import jwt

# standard libraries
import time

#fastapi
from fastapi import Depends

#typing
from typing import Dict

# .env
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

async def sign_jwt(user_id: str) -> str:
    
    payload = {
        "user_id": user_id,
        "expires": time.time() + 900
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        payload = decoded_token if decoded_token["expires"] >= time.time() else None
    
    except:
        payload = {}

    return payload



