# typing
from typing import List

# functions to be implement
from .dogs import dogs
from .auth import auth
from .users import users

# db
from .db import engine, database, metadata

# fastapi
from fastapi import FastAPI

# create schema db
metadata.create_all(engine)

app = FastAPI(title="Guane API")


# connecting to the database
@app.on_event("startup")
async def startup():
    await database.connect()

# disconnecting from the database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# auth route
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

# dogs routes
app.include_router(dogs.router, prefix="/api/dogs", tags=["dogs"])

# users routes
app.include_router(users.router, prefix="/api/users", tags=["users"])

