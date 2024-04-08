from data.entities.User import User, UserData
from domain.postgres.Pgconnection import Pgconnection
from domain.repository.IUserRepository import IUserRepository

# UserRepositoryImpl es la implementacion del repositorio de usuario

class UserRepositoryImpl(IUserRepository):

    def insert(self, entity: User):
        pass

    def update(self, entity: User):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        print("hrere")
        users = []
        connection = Pgconnection()
        conn = connection.datasource_pg()
        cur = conn.cursor()
        cur.execute('select * FROM public."Usuario"')
        rows = cur.fetchall()
        for row in rows:
            user = UserData(*row)
            users.append(user)
        cur.close()
        return users
