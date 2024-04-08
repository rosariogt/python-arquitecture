from unittest import TestCase

from useCaseImpl.UserServiceImpl import UserServiceImpl


class TestUserServiceImpl(TestCase):

    def test_obtener_todos(self):
        service = UserServiceImpl()
        response = service.obtenerTodos()
        print(response)
