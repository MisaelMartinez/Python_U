from fastapi import FastAPI
app = FastAPI()

cars_list: list[dict] =[
    {"car_name":"Elantra"},
    {"car_name":"Civic"},
    {"car_name":"Sentra"},
    {"car_name":"Corolla"}
]


@app.get("/cars/")
async def get_cars(limit: int =10, skip:int=0, opcional: str | None = None):
    if opcional:
        return f"Esto es una prueba de una entrada opcional: {opcional}"
    return cars_list[skip: skip + limit]


#?limit=3&skip=1 esto es lo que debemos poner despues de cars/   
#  http://127.0.0.1:8000/cars/?opcional=jdjdjdj