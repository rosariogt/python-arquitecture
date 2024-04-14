from unittest import TestCase

from domainImpl.repositories.UserRepositoryImpl import UserRepositoryImpl


class TestUserRepositoryImpl(TestCase):
    repository = UserRepositoryImpl()
    users = repository.getAll()
    print(users)
