from unittest import TestCase

from data.dto.Book import Book
from useCaseImpl.client.Client import Client

class TestClient(TestCase):
    apiUrl = "https://example-data.draftbit.com/books"
    client = Client()
    result = client.getRest(apiUrl);
    if( result.codeStatus == 200 ):
        data_dict = result.body
        data_list = [Book.parse_obj(item) for item in data_dict]
        print(data_list)
