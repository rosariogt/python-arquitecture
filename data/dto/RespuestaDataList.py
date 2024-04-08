from typing import TypeVar, List

from pydantic import BaseModel
from pydantic.fields import FieldInfo

# Clase Base, Define un tipo genérico T
T = TypeVar('T')

class RespuestaDataList(BaseModel):
    dataList: List[T] = []
    success: bool
    messages: List[str] = []

    # Setter
    def set_dataList(self, dataList):
        self.dataList = dataList

    def set_success(self, success):
        self.success = success

    def set_messages(self, messages):
        self.messages = messages

    def __str__(self) -> str:
        return f"(dataList={self.dataList}, success={self.success}, messages={self.messages})"


