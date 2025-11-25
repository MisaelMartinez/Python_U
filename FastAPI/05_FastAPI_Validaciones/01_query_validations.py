from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()
@app.get("/items/")
#Este es la linea original.
##async def read_items(q: str|None =None):
async def read_items(q: Annotated[list[str]|None,Query()] =None):
    results: dict = {"mensaje":"Acceso de get(read_items)"}
    if q:
        results.update({"q":q})
        return results
    

# En postman debemos de ingresar a la ruta http://127.0.0.1:8000/items/ en GET
# despues en key escribimos q y en value escribimos cualquier cosa. Nos debe de salir 
# http://127.0.0.1:8000/items/?q=algo&q=mas
# En este caso agregamos 2 q str y por eso no nos da error








