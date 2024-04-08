# This is a sample Python script.
import sys

from fastapi import FastAPI

from useCaseImpl.UserServiceImpl import UserServiceImpl

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print(sys.path)

app = FastAPI()
app.title = 'My app'
app.version = '0.0.1'

service = UserServiceImpl()

@app.get("/", tags= ['home'])
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def read_date():
    return service.obtenerTodos()