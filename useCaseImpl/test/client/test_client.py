from unittest import TestCase

from useCaseImpl.client.Client import Client


class TestClient(TestCase):
    client = Client()
    result = client.getBook();
    print("resultado", result)
