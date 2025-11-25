from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str|None=None
    price: float

class User(BaseModel):
    username: str[str, Field(min_length=5)]
    full_name:str|None=None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, p: Annotated[int, Body()]): #Body sirve para evitar que FastAPI interprete que no va en el query.
    return {"item_id": item_id, "item": item, "user": user}
