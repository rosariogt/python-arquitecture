from pydantic.dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class BookData():
    id:int
    title:str
    authors:str

class Book(BaseModel, BookData):
    pass