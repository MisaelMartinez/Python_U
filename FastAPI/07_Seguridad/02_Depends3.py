from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated

app = FastAPI()

def common_parameters(q: str|None = None, skip: int=0, limit: int  = 100):
    return {"q": q, "skip":skip, "limit": limit}

@app.get("/items/")
def get_items(commons:Annotated[dict, Depends(common_parameters)]):
    return commons







