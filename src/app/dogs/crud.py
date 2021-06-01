"""crud dogs module"""

# functions to be implement
from .models import DogSchema

# DB 
from app.db import dogs, database

# create db
async def post_dog(name: str, payload: DogSchema, dog_picture, dog_create_date):
    query = dogs.insert().values(name=name,
                                picture=dog_picture,
                                is_adopted=payload.is_adopted,
                                create_date=dog_create_date
                                )
    
    return await database.execute(query=query)

# get all db
async def get_all():
    query = dogs.select()
    
    return await database.fetch_all(query=query)

# get dogs adopted db
async def get_dog_adopted():
    query = dogs.select().where(dogs.c.is_adopted == True)

    return await database.fetch_all(query=query)

# get dog for name db
async def get_dog(name: str):
    query = dogs.select().where(name == dogs.c.name)

    return await database.fetch_one(query=query)

# update db
async def put_dog(name: str, payload:DogSchema):
    query = (
        dogs
        .update()
        .where(name == dogs.c.name)
        .values(is_adopted=payload.is_adopted)
        .returning(dogs.c.id)
        )

    return await database.execute(query=query)

# delete db
async def delete_dog(name: str):
    query = dogs.delete().where(name == dogs.c.name)

    return await database.execute(query=query)

