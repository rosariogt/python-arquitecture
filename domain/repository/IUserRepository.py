from data.entities.User import User
from domain.IRepository import IRepository

# IUserRepository definicion de metodos a implementar
class IUserRepository(IRepository):

    def create(self, entity: User):
        pass

    def update(self, entity: User):
        pass

    def getById(self, id: int):
        pass

    def getAll(self):
        pass
