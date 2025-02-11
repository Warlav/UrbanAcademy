from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin() -> dict:
    return {f"Вы вошли как администратор"}


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/age/{age}")
async def read_user(username: str, age: int) -> dict:
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
