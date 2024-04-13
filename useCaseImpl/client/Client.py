import requests

from data.dto.ResponseClient import ResponseClient

HEADERS = {'accept': 'application/json'}

class Client():

    def getRest(self, url):
        response = requests.get(url, headers=HEADERS)
        result = ResponseClient(response.status_code, response.json())
        return result

    def postRest(self, url, body):
        return requests.post(url, data=body, headers=HEADERS)

    def put(self, url, body):
        return requests.put(url, data=body, headers=HEADERS)
