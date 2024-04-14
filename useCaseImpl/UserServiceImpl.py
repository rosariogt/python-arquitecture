from data.dto.RespuestaDataList import RespuestaDataList
from domainImpl.repositories.UserRepositoryImpl import UserRepositoryImpl
from useCase.IUserService import IUserService


class UserServiceImpl(IUserService):

    def obtenerTodos(self):
        response = RespuestaDataList(dataList=[], success=False, messages=[])
        mensajesLista = []
        userRepository = UserRepositoryImpl()
        users = userRepository.getAll()
        if users == []:
            mensajesLista.append("NO SE ENCONTRARON RESULTADOS")
            response.set_messages(mensajesLista)
            return response
        response.set_success(True)
        response.set_dataList(users)
        return response
