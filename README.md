
Clean arquitectura

# instalar pydantic, para el manejo de los modelos(entities, dtos)
pip install -U pydantic

# instalar fastApi
pip install fastapi uvicorn

# conexion a postgres
pip install psycopg2

# levantar el servicio
uvicorn main:app --reload

# instalar request
pip install requests

python.exe -m pip install --upgrade pip

microservicio 1
proyecto 1 productos --> rest crear, obtener, actualizar

microservicio 2 (requiere de los servicios de productos, lista productos)
proyecto 2 ventas --> rest crear, obtener, actalizar
