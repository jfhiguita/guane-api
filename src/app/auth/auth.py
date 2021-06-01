"""user handler"""

# fastapi
from fastapi import APIRouter, HTTPException, status, Body

# functions to be implement
from .models import UserSchema, UserDB
#from .crud import 
from .utils import sign_jwt


router = APIRouter()

# create token
@router.post("/login", response_model=UserDB, status_code=201)
async def auth(payload: UserSchema = Body(...)):

    #await crud.post(payload, hash_password)
    token = await sign_jwt(payload.email)

    response_data = {
        "acces_token": token 
    }

    return response_data
    