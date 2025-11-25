from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()
#STRINGS
#max_length
#min_length
#pattern



# @app.get("/items/")                             #Longitud minima de 3. abc si es correcta.
# async def read_items(q: Annotated[str|None,Query(min_length=3)] =None):
#     results: dict = {"mensaje":"Acceso de get(read_items)"}
#     if q:
#         results.update({"q":q})
#         return results

#Validaciones para enteros
#gt: greater than, >
#ge: greater than or equal >=
#lt: less than, <
#le: less thn or equal<=

@app.get("/items/")              #INT           #numero debe de ser mayor que 3
async def read_items(q: Annotated[int|None,Query(gt=3)] =None): 
    results: dict = {"mensaje":"Acceso de get(read_items)"}
    if q:
        results.update({"q":q})
        return results