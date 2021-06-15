# Developing Asynchronous API with FastAPI, security JWT, PostgreSQL + SQLAlchemy, Celery + RabbitMQ, Redis and Docker

## Want to use this project?

Build the images and run the containers:

```sh
$ docker-compose up -d --build
```
Then, run DB migrations

```sh
$ docker-compose exec web alembic upgrade head
```

Test out the following routes:

1. [http://localhost:8002/api/dogs](http://localhost:8002/api/dogs)
2. [http://localhost:8002/api/users](http://localhost:8002/api/users)
3. [http://localhost:8002/api/auth/login](http://localhost:8002/api/auth/login)
4. [http://localhost:8002/redoc](http://localhost:8002/redoc)
