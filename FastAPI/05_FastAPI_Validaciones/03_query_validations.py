from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()
#METADATA
#titulo
#description
#alias
#deprecated

@app.get("/items/{item_id}")                           
async def read_items(q: Annotated[
    int|None,
    Query(gt=3,
          title="Query", 
          description="Lo que se buscara",
          alias="item_query",
          deprecated="True")
    ] =None):
    results: dict = {"mensaje":"Acceso de get(read_items)"}
    if q:
        results.update({"q":q})
        return results
    




























