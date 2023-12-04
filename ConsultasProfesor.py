import pymysql
from ConexionBBDD import conect


def consAlta(dni, nombre, direccion, telefono):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"INSERT INTO profesor (dni,nombre,direccion,telefono) VALUES ('{dni}','{nombre}','{direccion}','{telefono}')")
        conect.commit()
        cursor.close()
        print("Profesor guardado correctamente")
    except pymysql.Error as err:
        print(err)

def consBaja(dni):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"DELETE FROM profesor WHERE dni = '{dni}'")
        conect.commit()
        cursor.close()
        print("Profesor dado de baja correctamente")
    except pymysql.Error as err:
        print(err)

def consBusqueda(dni):
    try:
        cursor = conect.cursor()
        cursor.execute(f"SELECT * FROM profesor WHERE dni = '{dni}' ")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)

def mostrarTabla():
    try:
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM profesor")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)
