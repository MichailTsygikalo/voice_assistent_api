from pydantic import BaseModel

class Monument(BaseModel):
    id:int
    description:str
    photo:str
    name:str

    class Config:
        arbitrary_types_allowed = True

class Person(BaseModel):
    id:int
    description:str
    photo:str
    name:str
    
    class Config:
        arbitrary_types_allowed = True

class ShowMonument(BaseModel):
    monuments:list[Monument]

    class Config:
        arbitrary_types_allowed = True

class ShowPerson(BaseModel):
    persons:list[Person]

    class Config:
        arbitrary_types_allowed = True