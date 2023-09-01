import connect

# Datos para estudiantes
estudiantes = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20},
    {"nombre": "María", "apellido": "González", "edad": 22},
    {"nombre": "Carlos", "apellido": "López", "edad": 21},
    {"nombre": "Ana", "apellido": "Martínez", "edad": 19},
    {"nombre": "Luis", "apellido": "Rodríguez", "edad": 23},
    {"nombre": "Laura", "apellido": "Díaz", "edad": 20},
    {"nombre": "Sofía", "apellido": "Hernández", "edad": 22},
    {"nombre": "Pedro", "apellido": "Ramírez", "edad": 21},
    {"nombre": "Isabel", "apellido": "Sánchez", "edad": 19},
    {"nombre": "Fernando", "apellido": "Gómez", "edad": 23},
    {"nombre": "Rosa", "apellido": "Torres", "edad": 20},
]

# Datos para cursos
cursos = [
    {"nombre_curso": "Matemáticas", "id_estudiante": 1},
    {"nombre_curso": "Historia", "id_estudiante": 2},
    {"nombre_curso": "Física", "id_estudiante": 3},
    {"nombre_curso": "Literatura", "id_estudiante": 4},
    {"nombre_curso": "Programación", "id_estudiante": 5},
    {"nombre_curso": "Inglés", "id_estudiante": 6},
    {"nombre_curso": "Química", "id_estudiante": 7},
    {"nombre_curso": "Biología", "id_estudiante": 8},
    {"nombre_curso": "Economía", "id_estudiante": 9},
    {"nombre_curso": "Arte", "id_estudiante": 10},
]

# Abrir la conexión con la base de datos
connection = connect.make_connection()
# Crear el cursor para modificar la base
cursor = connection.cursor()

for estudiante in estudiantes:
    query = "INSERT INTO estudiante (nombre, apellido, edad) VALUES (%s, %s, %s)"
    cursor.execute(
        query, (estudiante["nombre"], estudiante["apellido"], estudiante["edad"])
    )
connection.commit()

for curso in cursos:
    query = "INSERT INTO curso (nombre_curso, id_estudiante) VALUES (%s, %s)"
    cursor.execute(query, (curso["nombre_curso"], curso["id_estudiante"]))
connection.commit()

# Cerrar la conexión
connect.close_connection(connection)
