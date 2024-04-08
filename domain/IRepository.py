from abc import ABC, abstractmethod

from pydantic import BaseModel

# Clase Base de repositorios

class IRepository(ABC):

    @abstractmethod
    def create(self, entity: BaseModel):
        pass

    @abstractmethod
    def update(self, entity: BaseModel):
        pass

    @abstractmethod
    def getById(self, id: int):
        pass

    @abstractmethod
    def getAll(self):
        pass
