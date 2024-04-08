import psycopg2

from domain.postgres.config import config


class Pgconnection:

    def datasource_pg(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print("Connected succesfully ", db_version)
            cur.close()
        except (Exception) as error:
            print(error)
        return conn

    def connect(self):
        conn = None
        try:
            # Leemos los parámetros de conexión
            params = config()

            # Conectamos con el servidor PostgreSQL
            print('Conectando con PostgreSQL...')
            conn = psycopg2.connect(**params)

            # creamos un cursor
            cur = conn.cursor()

            # Ejecutamos una sentencia SQL
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # Mostramos la versión de PostgreSQL que hemos solicitado con la sentencia anterior
            db_version = cur.fetchone()
            print(db_version)

            # Cerramos la comunicación con PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
