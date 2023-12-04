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


def consBusqueda(nombre):
    try:
        cursor = conect.cursor()
        cursor.execute(f"SELECT * FROM curso WHERE nombre = '{nombre}' ")
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
