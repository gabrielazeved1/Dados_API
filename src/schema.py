from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados,a view da api
    name: str
    type: str
    
    class Config:
        orm_mode = True