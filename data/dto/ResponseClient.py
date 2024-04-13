
'''
@author: rosariogt
@date: 12/04/2024

@description: clase que permite obtener el code status http y el body
'''

class ResponseClient():

    def __init__(self, codeStatus, body):
        self.codeStatus = codeStatus
        self.body = body