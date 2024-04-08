from dataclasses import dataclass
from datetime import date
from typing import Optional

from pydantic import BaseModel

@dataclass
class UserData():
    id: int
    nombre: str
    materno: str
    paterno: str
    login: str
    password: str
    id_unidad: int
    habilitar: int
    admin: int
    date_usuario: Optional[date]

class User(BaseModel, UserData):
    pass