"""Crud users module"""

# functions to be implement
from .models import UserSchema

# DB
from ..db import users, database

#create user db
async def post_user(name: str, last_name: str, payload: UserSchema):
    query = users.insert().values(name=name,
                                  last_name=last_name,
                                  email=payload.email
                                  )
    return await database.execute(query=query)

# get all users db
async def get_all():
    query = users.select()

    return await database.fetch_all(query=query)

# get user db
async def get_user(name: str, last_name: str):
    query = users.select().where((name == users.c.name) &
                                (last_name == users.c.last_name))

    return await database.fetch_one(query=query)

# update user db
async def put_user(name: str, last_name: str, payload: UserSchema):
    query = (
        users
        .update()
        .where((name == users.c.name) & (last_name == users.c.last_name))
        .values(email=payload.email)
        .returning(users.c.id)
    )

    return await database.execute(query=query)

# delete user db
async def delete_user(name: str, last_name: str):
    query = users.delete().where((name == users.c.name) & (last_name == users.c.last_name))

    return await database.execute(query=query)
