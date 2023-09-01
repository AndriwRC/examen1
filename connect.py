import mysql.connector

# Configura los parámetros de conexión
config = {
    "user": "public",
    "password": "42PzVD!K",
    "host": "localhost",
    "database": "tallerdb",
    "port": 3306,
}


# Crea una conexión a la base de datos
def make_connection():
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexión a la base de datos exitosa.")

    return connection


def close_connection(connection):
    # Cierra la conexión cuando hayas terminado
    if "connection" in locals():
        connection.close()
        print("Conexión cerrada.")
