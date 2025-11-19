from enum import Enum
from fastapi import FastAPI

class CarDealer(Enum):
    HONDA = 'honda'
    BMW = 'bmw'
    FORD =  'ford'

app = FastAPI()
@app.get("/models/msj")
async def get_model2():
    return {"message": "Esto no corresponde a ningun car_dealer"}
#Esto hara caso siempre que sea un static y despues un dinamico.


@app.get("/models/{car_dealer}")
async def get_model(car_dealer: CarDealer):
    if car_dealer is CarDealer.HONDA:
        return {"car_dealer": car_dealer, "message": "Honda es Japones"}
    if car_dealer is CarDealer.BMW:
        return {"car_dealer": car_dealer, "message": "BMW es Alemana"}
    return {"car_dealer": car_dealer, "message": "FORD es gringa"}



