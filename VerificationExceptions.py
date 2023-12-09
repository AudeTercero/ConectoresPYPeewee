from datetime import datetime

import ConsultasAlumnos
import ConsultasInscripciones
import ConsultasProfesor
import ConsultasCurso


class MisExceptions(Exception):
    """
    Clase creada para generar nuestras propias excepciones
    """

    def __init__(self, message="Error"):
        self.message = message

        super().__init__(self.message)


def hayAlgo(cadena):
    """
    Verifica que la cadena no este vacia
    Si lo esta, lanza una excepcion
    :param cadena: La cadena a validar
    :return:
    """
    if len(cadena) == 0:
        raise MisExceptions('No se ha escrito nada')


def dniFormat(dni):
    """
    Verifica que un DNI recibido tenga el formato correcto
    Lanza una excepcion u otra dependiendo del problema
    :param dni: El DNI a validar
    :return:
    """
    # Se eliminan espacios de los laterales
    dni = dni.strip()
    if len(dni) != 9:
        raise MisExceptions('Debe tener 9 caracteres')
    if not dni[:-1].isdigit():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')
    if not dni[-1].isalpha():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')


def validar_telefono(telefono):
    """
    Verifica que un telefono tenga la extension correcta
    Ademas comprueba que sea un digito
    En caso contrario lanza una excepcion
    :param telefono: El telefono a validar
    :return:
    """
    # Se eliminan espacios de los laterales
    telefono = telefono.strip()

    # Verificamos si el numero de telefono tiene exactamente 9 digitos
    if not telefono.isdigit() or len(telefono) != 9:
        raise MisExceptions("El numero de telefono debe tener exactamente 9 digitos.")


def esNum(num):
    """
    Verifica que el numero introducido sea un numero
    En caso contrario lanza una excepcion
    :param num: El numero a validar
    :return:
    """
    if type(num) != int:
        raise MisExceptions('Debe introducir solo numeros')


def formatoFecha(fecha):
    """
    Verifica que la fecha introducida tenga el formato correcto
    En caso contrario lanza una excepcion
    :param fecha: La fecha a validar
    :return:
    """
    formato = "%Y-%m-%d"
    try:
        datetime.strptime(fecha, formato)
    except ValueError:
        raise MisExceptions('Formato de la fecha incorrecto. Formato esperado yyyy-mm-dd')


def existDni(dni):
    """
    Comprueba que no exista ya un DNI
    :param dni: El DNI a buscar
    :return:
    """
    if ConsultasProfesor.existProfesor(dni):
        raise MisExceptions('Ya existe un profesor con ese dni')


def noExistDni(dni):
    """
    Comprueba que si exista un DNI
    :param dni: El DNI a buscar
    :return:
    """
    if not ConsultasProfesor.existProfesor(dni):
        raise MisExceptions('No se ha encontrado un profesor con ese dni')


def existNombreCur(nombre):
    """
    Comprueba que no exista un Curso con ese nombre
    :param nombre: El nombre a buscar
    :return:
    """
    if ConsultasCurso.existeCurso(nombre):
        raise MisExceptions('Ya existe un curso con ese nombre')


def noExistNombreCur(nombre):
    """
    Comprueba que si exista un curso con ese nombre
    :param nombre: El nombre a buscar
    :return:
    """
    if not ConsultasCurso.existeCurso(nombre):
        raise MisExceptions('No se ha encontrado un curso con ese nombre')


def existeAlumno(nombre, apellidos):
    """
    Comprueba que no exista un Alumno con el nombre y apellidos recibidos
    :param nombre: El nombre a comprobar
    :param apellidos: Los apellidos a comprobar
    :return:
    """
    if ConsultasAlumnos.existeAlumno(nombre, apellidos):
        raise MisExceptions('Ya existe un alumno con ese nombre y apellidos')


def noExisteAlumno(nombre, apellidos):
    """
    Comprueba que si exista un Alumno con el nombre y apellidos recibidos
    :param nombre: El nombre a comprobar
    :param apellidos: Los apellidos a comprobar
    :return:
    """
    if not ConsultasAlumnos.existeAlumno(nombre, apellidos):
        raise MisExceptions('No se ha encontrado un alumno con ese nombre y apellidos')


def noExisteAlumnoEnAlumnoCurso(idAlumno, idCurso):
    """
    Comprueba que exista un alumno en un curso concreto
    :param idAlumno: El id del alumno a buscar
    :param idCurso: El id del Curso donde se busca
    :return:
    """
    if not ConsultasInscripciones.existeAluEnAluCurso(idAlumno, idCurso):
        raise MisExceptions('No se ha encontrado un alumno con ese nombre y apellidos en ese curso')


def existeAlumnoEnAlumnoCurso(idAlumno, idCurso):
    """
    Comprueba que no exista un alumno en un curso concreto
    :param idAlumno: El id del alumno a buscar
    :param idCurso: El id del Curso donde se busca
    :return:
    """
    if ConsultasInscripciones.existeAluEnAluCurso(idAlumno, idCurso):
        raise MisExceptions('Ese alumno ya esta matriculado en ese curso')


def noExisteProfesorEnCurso(idProfesor, idCurso):
    """
    Comprueba que exista un profesor en un curso concreto
    :param idProfesor: El id del profesor que se busca
    :param idCurso: El id del curso donde se busca
    :return:
    """
    if not ConsultasInscripciones.existeProfEnCurso(idProfesor, idCurso):
        raise MisExceptions('No se ha encontrado un profesor con ese dni en ese curso')


def existeProfesorEnCurso(idProfesor, idCurso):
    """
    Comprueba que no exista un profesor en un curso concreto
    :param idProfesor: El id del profesor que se busca
    :param idCurso: El id del curso donde se busca
    :return:
    """
    if ConsultasInscripciones.existeProfEnCurso(idProfesor, idCurso):
        raise MisExceptions('Ese profesor ya esta matriculado en ese curso')


def equals_ignore_case(str1, str2):
    """
    Funcion que verifica si dos cadenas son iguales independientemente de las mayusculas o minusculas
    :param str1: Recibe una cadena para compararla con la otra
    :param str2: Recibe la otra cadena para compararla con la primera
    :return: Retorna si son iguales o no
    """
    return str1.lower() == str2.lower()
