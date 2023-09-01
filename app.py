from flask import Flask
import connect

# Abrir la conexión con la base de datos
connection = connect.make_connection()
# Crear el cursor para modificar la base
cursor = connection.cursor()
cursor.execute("SELECT * FROM estudiante;")
estudiantes = cursor.fetchall()
cursor.execute("SELECT * FROM curso;")
cursos = cursor.fetchall()


app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Estudiantes</h1><p>{estudiantes}</p><h1>Cursos</h1><p>{cursos}</p>"


# Cerrar la conexión
connect.close_connection(connection)
