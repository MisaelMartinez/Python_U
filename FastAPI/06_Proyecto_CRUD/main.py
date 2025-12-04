#Este proyecto se aplicara todo lo aprendido en la carpeta 1,2 y 5.
# Clase 1: Crea una clase (Mode de pydantic) llamada "Tarea". 
# Con id numerico mayor a cero,
# con titulo string longitud minima de 3
# Estado string que pueda ser unicamente pendiente o completo. (default pendiente.)
# Crea una fake_db que sea una lista de al menos 10 Tareas

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from itertools import count #Para los id, genera id.

id_gen = count(start=1)
def obt_newid() -> int:
    return next(id_gen)
#Esto es lo que todas nuestras tareas deben de tener obligatoriamente
class TareaBase(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    estado: Literal["Pendiente", "Completo"] = "Pendiente" 

class TareaCreate(TareaBase):
    pass

class TareaUpdate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    estado: Literal["Pendiente", "Completo"]

class Tarea(TareaBase): #Hereda de TareaBase y ya tiene titulo y estado.
    id: Annotated[int, Field(gt=0)]

fake_list = [
    Tarea(id=obt_newid(), title="Tender cama"),
    Tarea(id=obt_newid(), title="Tomar una ducha"),
    Tarea(id=obt_newid(), title="Barrer sala", estado="Completo"),
    Tarea(id=obt_newid(), title="Estudiar Python"),
    Tarea(id=obt_newid(), title="Comer fruta"),
    Tarea(id=obt_newid(), title="Lavar trastes"),
    Tarea(id=obt_newid(), title="Hacer ejercicio",estado="Completo"),
    Tarea(id=obt_newid(), title="Comprar comida",estado="Completo"),
    Tarea(id=obt_newid(), title="Hacer de comer",estado="Completo"),
    Tarea(id=obt_newid(), title="Revisar moto"),

]

#Crear el app de FastAPI y la ruta /tareas/ con GET.
#Crear modelo de filtro, FILTERPARAMS con 
    #limit >=1 (delfault 5)
    #offset >=0 (default 0)
    #Estado (opcional)
#Utiliza el estado para filtrar las tareas y despues de filtrarlas utilizar offset y limit para devolver las correctas.

class FilterParams(BaseModel):
    limit: Annotated[int, Field(gt=0)] = 5
    offset: Annotated[int, Field(ge=0)] = 0
    estado: Literal["Pendiente","Completo"] |None = None
    search: str | None = None #Busca en el titulo alguna cadena de caracteres.


app = FastAPI()

@app.get("/tareas/", response_model=list[Tarea])
async def get_tareas(filter: Annotated[FilterParams, Query()]):
    
    # #Forma larga
    # if filter.estado:
    #     tareas_filtradas = [tarea for tarea in fake_list if tarea.estado == filter.estado]
    # else:
    #     tareas_filtradas = fake_list

    tareas_filtradas = (
        [tarea for tarea in fake_list if tarea.estado == filter.estado] if filter.estado else fake_list
    )
    #   Filtrado por search.
    if filter.search:
        tareas_filtradas = [
            t for t in tareas_filtradas if filter.search.lower() in t.title.lower() #Minusculas.
        ]

    #Aplicar paginacion 
    return tareas_filtradas[filter.offset: filter.offset + filter.limit]

@app.get("/tareas/{id}", response_model=Tarea)
async def get_tareas_id(id: int):
    for tarea in fake_list:
        if tarea.id == id:
            return tarea
    raise HTTPException(status_code=404, detail="Not found nothing nothing")

@app.post("/tareas/", response_model= Tarea, status_code= 201)
async def crear_tareas(tarea: TareaCreate):
    new_id : int = obt_newid()
    new_tarea : Tarea = Tarea(id=new_id, **tarea.model_dump()) 
    fake_list.append(new_tarea)
    return new_tarea

# Para insertar una nueva tarea es necesario ingresar a postman
# ir al body - raw - JSON.
# escribir lo siguiente 
# {
#     "title":"Reservar una Comer",
#     "estado":"Pendiente",
#     "id":12
# }
# y por ultimo SEND

#METODO PUT, Actualizar tareas.

@app.put("/tareas/{id}", response_model=Tarea)
async def actualizar_tarea(id: int,datos:TareaUpdate):
    for i, tarea in enumerate(fake_list):
        if tarea.id == id:
            tarea_act = tarea.model_copy(update=datos.model_dump())#Esto viene de fastapi
            fake_list[i] = tarea_act
            return tarea_act
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#Crear una request con PUT. en postman
#http://127.0.0.1:8000/tareas/2
#Body-row,JSON, y datos a actualizar
# {
#     "title":"Probando PUT, Ya me bañe",
#     "estado":"Completo"
# }
# Fin, Probar los cambios con un GET y el id en la url

@app.delete("/tareas/{id}",status_code=204)
async def eliminar_tarea(id: int):
    for i, tarea in enumerate(fake_list):
        if tarea.id == id:
            del fake_list[i]
            return
    raise HTTPException(status_code=404, detail="Tarea no encontrada.")


