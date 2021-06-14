"""Models dog module"""


#standard libraries
from datetime import datetime

# Pydantic models
from pydantic import BaseModel


# dog schema
class DogSchema(BaseModel):
    is_adopted: bool 
    id_user: int

# dog model
class DogDB(DogSchema):
    id: int
    name: str
    picture: str = 'http://example.com/picture'
    create_date: datetime

