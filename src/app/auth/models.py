"""Models auth module"""

# standard libraries

# pydantic models
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


# user login schema
class UserSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "example@guane.com",
                "password": "pass_word"
            }
        }

# user model
class UserDB(BaseModel):
    acces_token: str = Field(...)