from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}


@app.post("/products/")
async def create_product():
    # name: str
    # price: float
    # quantity: int
    """
    Создает новый продукт в системе.
    - **name**: название продукта
    - **price**: цена продукта
    - **quantity**: количество на складе
    """
    return


@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello, Urban’s student!"}


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"User {user_id}"}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10) -> dict:
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    return {"items": items}


