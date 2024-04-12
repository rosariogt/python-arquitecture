import requests

from data.dto.Book import Book

class Client():


    def getBook(self):
        URL = 'https://example-data.draftbit.com/books'

        response = requests.get(URL)
        HEADERS = {'accept': 'application/json'}

        response = requests.get(URL, headers=HEADERS)

        if response.status_code == 200:
            print("Peticion exitosa")

            #print(response.content)
            data_dict = response.json()
            #my_model_instance = Book.parse_obj(data_dict)
            data_list = [Book.parse_obj(item) for item in data_dict]

            print(data_list)