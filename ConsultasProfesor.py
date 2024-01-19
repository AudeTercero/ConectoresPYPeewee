import pymysql
from ConexionBBDD import conect
import Tablas_BBDD


def consAlta(dni, nombre, direccion, telefono):
    con = Tablas_BBDD.conexion()
    """
    Funcion que lanza una una insreccion en la tabla de profesor de la base de datos
    :param dni: Recibe el dni para
    :param nombre: Recibe el nombre
    :param direccion: Recibe la direccion
    :param telefono: Recibe el telefono
    :return:
    """
    Tablas_BBDD.Profesor.create(name=nombre, dni=dni, direccion=direccion, telefono=telefono)
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
    """
    Funcion que que borra un profesor de la base de datos
    :param dni: Recibe el dni del profesor a borrar
    :return:
    """
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
    """
    Funcion para buscar un profesor en la base de datos
    :param dni: Recibe el dni del profesor a buscar
    :return: Retorna el resultado del select
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"SELECT p.*, GROUP_CONCAT(c.nombre) AS nombre_curso FROM profesor p LEFT JOIN curso c ON p.id = c.id_profesor WHERE p.dni = '{dni}' GROUP BY p.id")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def consModificar(dni, columna, nuevoCampo):
    """
    Funcion para modificar un profesor
    :param dni: Recibe el dni del profesor a modificar
    :param columna: Recibe la columna del campo que queremos modificar
    :param nuevoCampo: Recibe el nuevo campo a modificar
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE profesor SET {columna} = '{nuevoCampo}' WHERE dni = '{dni}'")
        con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)


def mostrarTabla():
    """
    Funcion que obtiene de la base de datos todos los datos de todos los profesores
    :return: Retorna todos los resultados para mostrarlos
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT profesor.*, GROUP_CONCAT(curso.nombre) AS nombre_curso FROM profesor LEFT JOIN curso ON profesor.id = curso.id_profesor GROUP BY profesor.id")
        resultados = cursor.fetchall()

        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def existProfesor(dni):
    """
    Funcion para comporobar si existe o no un profesor
    :param dni: Recibe el dni del profesor
    :return: Retorna si existe o no
    """
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
def hayProfesores():
    """
    Funcion que comprueba si hay profesores dados de alta
    :return: Retorna booleano si lo hay o no
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM profesor")
        resultados = cursor.fetchall()
        cursor.close()
        if resultados:
            return True
    except pymysql.Error as err:
        print(err)
    print('\nAun no hay profesores dados de alta')
    return False
