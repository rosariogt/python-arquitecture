from typing import TypeVar
from pydantic import BaseModel
from typing import List, Optional

# Clase base, define un tipo genérico T

T = TypeVar('T')

class RespuestaData(BaseModel):
    data: T
    success: bool
    messages: List[str] = []

    def set_data(self, data):
        self.data = data

    def set_success(self, success):
        self.success = success

    def set_messages(self, messages):
        self.messages = messages
