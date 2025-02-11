from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    age: int


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin() -> dict:
    return {f"Вы вошли как администратор"}


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def read_user(user: User) -> dict:
    return {f"Информация о пользователе. Имя: {user.username}, Возраст: {user.age}"}
