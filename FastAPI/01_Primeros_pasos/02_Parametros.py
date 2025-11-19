from fastapi import FastAPI
app = FastAPI()

@app.get("/books/fav")
async def get_book2():
    return {"Mi libro favorito es": "100 años de soledad"}

#Si tienen la misma ruta, por ejemplo /books entonces el estatico debe de ir primero. el dinamico despues.

@app.get("/books/{book_id}") #Se espera un id, es dinamico en la peticion 
async def get_book(book_id:int):
    return {"book_id": book_id}


# @app.get("/books")
# async def get_book2():
#     return [1,2,3,4,5]

# @app.get("/books")
# async def get_book3():
#     return [6,7,7,8,9]
#Siempre le hara caso al primero que aparezca porque son repetidos, el segundo nunca aparecera.




"""
Ahora vamos a ingresar a la siguiente direccion 
http://127.0.0.1:8000/books/book_id

El book_id puede ser 1,2,3,4,5, etc.
y books es porque nosotros pusimos esa ruta en la linea 3.

Ahora en la linea 5 si ponemos dentro del parantesis (book_id: int) en chrome nos saldra como int 
ya sin comillas
Esto genero que solo funcione con int. si enviamos una cadena nos muestra error o warning diciendo que 
deberia de ser int y no str. Esto gracias a que FA, utiliza pydanthic.

"""