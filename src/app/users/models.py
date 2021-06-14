"""Users model"""

#pydantic models
from pydantic import BaseModel
from pydantic.networks import EmailStr


# user schema
class UserSchema(BaseModel):
    email: EmailStr

# user model
class UserDB(UserSchema):
    id: int
    name: str
    last_name: str
