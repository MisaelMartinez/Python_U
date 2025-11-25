from typing import Annotated
from pydantic import AfterValidator, BaseModel


x: Annotated[int, "positivo", "id del usuario"] #Despues del int son metadatos.
#Pydantic usa Annotated para hacer validaciones.

def par(value: int) -> int:
    if value%2 ==1:
        raise ValueError(f'{value} no es numero par') #Si no es par entonces esto se retorna
    return value 

NumeroPar = Annotated[int, AfterValidator(par)] #After es un tipo de validator de pydantic
#Tiene 4 tipos
#After: Corre despues de las validacciones de pydantic
#Before:Corre antes de las validaciones de pydantic. Si viene como str en un int, truena el programa.
#Plain: Similar a before, termina al retornar el vahlor.
#Wrap: Flexibles, antes o despues de las validaciones de pydantic.

class Model1(BaseModel):
    my_number: NumeroPar#

class Model2(BaseModel):
    my_number2: Annotated[NumeroPar,AfterValidator(lambda v: v+1)]
class Model3(BaseModel):
    lista_pares:list[NumeroPar]


ejemplo: Model1 = Model1(my_number = 2)
ejemplo2: Model2 = Model2(my_number2 = 32)
print(ejemplo2)

ejemplo3: Model3 = Model3(lista_pares=[2,4,6])

#Este programa debe de tener activado el entorno virtual e instalado pydantic 
#python -m venv venv

