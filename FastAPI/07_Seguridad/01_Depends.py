from fastapi import FastAPI, Depends,HTTPException
from typing import Annotated

app = FastAPI()

class logger:
    def log(self, message:str)-> None:
        print(f'Loggin message: {message}')

def get_logger():
    return logger()

logger_dependency = Annotated[logger, Depends(get_logger)]

@app.get("/items/{message}")
def get_items(message: str, logger: logger_dependency):
    logger.log(message)
    return message

@app.get("/products/{message}")
def get_products(message:str, logger: logger_dependency):
    logger.log(message)
    return message














