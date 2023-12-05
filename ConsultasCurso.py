import pymysql
from ConexionBBDD import conect


def consAlta(nombre, descripcion):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"INSERT INTO curso (nombre,descripcion) VALUES ('{nombre}','{descripcion}')")
        conect.commit()
        cursor.close()
        print("Curso guardado correctamente")
    except pymysql.Error as err:
        print(err)


def consBaja(nombre):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"DELETE FROM curso WHERE nombre = '{nombre}'")
        conect.commit()
        cursor.close()
        print("Curso dado de baja correctamente")
    except pymysql.Error as err:
        print(err)


def consBusqueda(nombre):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"SELECT c.*, a.(nombre,apellidos) AS nombreCompleto, p.nombre FROM cursos c LEFT JOIN alumno a ON c.id = c.id_profesor WHERE dni = '{nombre}'")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def mostrarTabla():
    try:
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM curso")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def existeCurso(nombre):
    try:
        cursor = conect.cursor()
        cursor.execute(f"SELECT nombre FROM curso WHERE nombre = '{nombre}'")
        resultados = cursor.fetchall()
        cursor.close()
        if len(resultados) and resultados[0][0] == nombre:
            return True
    except pymysql.Error as err:
        print(err)

    return False
