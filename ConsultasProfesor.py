# import pymysql
from ConexionBBDD import conect
from Tablas_BBDD import Profesor
from Tablas_BBDD import Curso
from peewee import *
from Utiles import *

def consAlta(dni, nombre, direccion, telefono):
    """
    Funcion que lanza una una insreccion en la tabla de profesor de la base de datos
    :param dni: Recibe el dni para
    :param nombre: Recibe el nombre
    :param direccion: Recibe la direccion
    :param telefono: Recibe el telefono
    :return:
    """
    Profesor.create(nombre=nombre, dni=dni, direccion=direccion, telefono=telefono)
    print("Profesor guardado con exito")


def consBaja(dni):
    """
    Funcion que que borra un profesor de la base de datos
    :param dni: Recibe el dni del profesor a borrar
    :return:
    """

    Profesor.delete().where(Profesor.dni == dni).execute()
    verde("Profesor eliminado con exito")


def consBusqueda(dni):
    """
    Funcion para buscar un profesor en la base de datos
    :param dni: Recibe el dni del profesor a buscar
    :return: Retorna el resultado del select
    """
    query = (Profesor
             .select(Profesor, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_curso'))
             .left_outer_join(Curso, on=(Profesor.id == Curso.id_profesor_id))
             .where(Profesor.dni == dni)
             .group_by(Profesor.id))
    return query


def consModificar(dni, columna, nuevoCampo):
    """
    Funcion para modificar un profesor
    :param dni: Recibe el dni del profesor a modificar
    :param columna: Recibe la columna del campo que queremos modificar
    :param nuevoCampo: Recibe el nuevo campo a modificar
    :return:
    """
    Profesor.update({columna: nuevoCampo}).where(Profesor.dni == dni).execute()

def mostrarTabla():
    """
    Funcion que obtiene de la base de datos todos los datos de todos los profesores
    :return: Retorna todos los resultados para mostrarlos
    """
    query = (Profesor
             .select(Profesor, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_curso'))
             .left_outer_join(Curso, on=(Profesor.id == Curso.id_profesor_id))
             .group_by(Profesor.id))
    return query


def existProfesor(dni):
    """
    Funcion para comporobar si existe o no un profesor
    :param dni: Recibe el dni del profesor
    :return: Retorna si existe o no
    """
    query = Profesor.select().where(Profesor.dni == dni)
    if query.count() > 0:
        return True
    else:
        return False


def hayProfesores():
    """
    Funcion que comprueba si hay profesores dados de alta
    :return: Retorna booleano si lo hay o no
    """
    query = Profesor.select()
    if query.count() > 0:
        return True
    else:
        amarillo('\nAun no hay profesores dados de alta')
        return False
