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


@app.get("/users/me")
async def read_current_user() -> dict:
    return {"user": "This is the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"User {user_id}"}


@app.get("/products/{product_id}")
async def read_product(product_id: int, details: bool = False) -> dict:
    product_info = {"product_id": product_id, "name": f"Product {product_id}"}
    if details:
        product_info["details"] = "Detailed product information"
    return product_info


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10) -> dict:
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    return {"items": items}


@app.get("/items/new")
async def read_new_items() -> dict:
    return {"message": "This is a list of new items"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.get("/categories/{category_id}/items/{item_id}")
async def read_category_item(category_id: int, item_id: int) -> dict:
    return {"category_id": category_id, "item_id": item_id}
