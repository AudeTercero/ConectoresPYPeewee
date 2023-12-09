import pymysql
from ConexionBBDD import conect



def consAlta(dni, nombre, direccion, telefono):
    con = conect()
    """
    Funcion que lanza una una insreccion en la tabla de profesor de la base de datos
    :param dni: Recibe el dni para
    :param nombre: Recibe el nombre
    :param direccion: Recibe la direccion
    :param telefono: Recibe el telefono
    :return:
    """
    try:
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO profesor (dni,nombre,direccion,telefono) VALUES ('{dni}','{nombre}','{direccion}','{telefono}')")
        con.commit()
        cursor.close()
        print("Profesor guardado correctamente")
    except pymysql.Error as err:
        print(err)


def consBaja(dni):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"DELETE FROM profesor WHERE dni = '{dni}'")
        con.commit()
        cursor.close()
        print("Profesor dado de baja correctamente")
    except pymysql.Error as err:
        print(err)


def consBusqueda(dni):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT p.*, c.nombre AS nombre_curso FROM profesor p LEFT JOIN curso c ON p.id = c.id_profesor WHERE p.dni = '{dni}'")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def consModificar(dni, columna, nuevoCampo):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE profesor SET {columna} = '{nuevoCampo}' WHERE dni = '{dni}'")
        resultados = cursor.fetchall()
        con.commit()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def mostrarTabla():
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT p.*, c.nombre AS nombre_curso FROM profesor p LEFT JOIN curso c ON p.id = c.id_profesor")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def existProfesor(dni):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT dni FROM profesor WHERE dni = '{dni}'")
        resultados = cursor.fetchall()
        cursor.close()
        if (len(resultados) and resultados[0][0] == dni):
            return True
    except pymysql.Error as err:
        print(err)

    return False
