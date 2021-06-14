"""Users route"""

#fastapi
from typing import List
from fastapi import APIRouter,HTTPException
from fastapi.params import Path

#functions to be implement
from . import crud
from .models import UserSchema, UserDB


router = APIRouter()

# create user
@router.post("/{name}-{last_name}", response_model=UserDB, response_model_exclude_unset=True, status_code=201)
async def user(*,
    name: str = Path(..., title="Name of the user", min_length=3, max_length=50),
    last_name: str = Path(..., title="Last name of the user", min_length=3, max_length=50),
    payload: UserSchema):

    if await crud.get_user(name, last_name):
        raise HTTPException(status_code=409, detail="User is already in use")
    
    user_idx = await crud.post_user(name, last_name, payload)

    response_object = {
        "id": user_idx,
        "name": name,
        "last_name": last_name,
        "email": payload.email,
    }

    return response_object

# get all users
@router.get("/", response_model=List[UserDB], response_model_exclude_unset=True)
async def users():
    return await crud.get_all()

# get user for name and last name
@router.get("/{name}-{last_name}", response_model=UserDB, response_model_exclude_unset=True)
async def user_name(name: str, last_name: str):
    user = await crud.get_user(name, last_name)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# update user
@router.put("/{name}-{last_name}", response_model=UserDB, response_model_exclude_unset=True)
async def update_user(name: str, last_name: str, payload: UserSchema):
    user = await crud.get_user(name, last_name)
    user = dict(user.items())

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_idx = await crud.put_user(name, last_name, payload)

    response_object = {
        "id": user_idx,
        "name": name,
        "last_name": last_name,
        "email": user["email"],
    }

    return response_object

# delete user
@router.delete("/{name}-{last_name}", response_model=UserDB, response_model_exclude_unset=True)
async def delete(name: str, last_name: str):
    user = await crud.get_user(name, last_name)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await crud.delete_user(name, last_name)

    return user