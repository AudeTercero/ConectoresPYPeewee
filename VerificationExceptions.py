from datetime import datetime

import ConsultasAlumnos
import ConsultasInscripciones
import ConsultasProfesor
import ConsultasCurso


class MisExceptions(Exception):
    def __init__(self, message="Error"):
        self.message = message

        super().__init__(self.message)


def hayAlgo(cadena):
    if (len(cadena) == 0):
        raise MisExceptions('No se ha escrito nada')


def dniFormat(dni):
    if len(dni) != 9:
        raise MisExceptions('Debe tener 9 caractres')
    if not dni[:-1].isdigit():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')
    if not dni[-1].isalpha():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')


def validar_telefono(telefono):
    # Se eliminan espacios de los laterales
    telefono = telefono.strip()

    # Verificamos si el numero de telefono tiene exactamente 9 digitos
    if not telefono.isdigit() or len(telefono) != 9:
        raise ValueError("El numero de telefono debe tener exactamente 9 digitos.")


def esNum(num):
    if type(num) != int:
        raise MisExceptions('Debe introducir solo numeros')


def formatoFecha(fecha):
    formato = "%Y-%m-%d"
    try:
        datetime.strptime(fecha, formato)
    except ValueError:
        raise MisExceptions('Formato de la fecha incorrecto. Formato esperado yyyy-mm-dd')


def existDni(dni):
    if (ConsultasProfesor.existProfesor(dni)):
        raise MisExceptions('Ya existe un profesor con ese dni')


def noExistDni(dni):
    if (not ConsultasProfesor.existProfesor(dni)):
        raise MisExceptions('No se ha encontrado un profesor con ese dni')


def existNombreCur(nombre):
    if ConsultasCurso.existeCurso(nombre):
        raise MisExceptions('Ya existe un curso con ese nombre')


def noExistNombreCur(nombre):
    if not ConsultasCurso.existeCurso(nombre):
        raise MisExceptions('No se ha encontrado un curso con ese nombre')


def existeAlumno(nombre, apellidos):
    if ConsultasAlumnos.existeAlumno(nombre, apellidos):
        raise MisExceptions('Ya existe un alumno con ese nombre y apellidos')


def noExisteAlumno(nombre, apellidos):
    if not ConsultasAlumnos.existeAlumno(nombre, apellidos):
        raise MisExceptions('No se ha encontrado un alumno con ese nombre y apellidos')


def noExisteAlumnoEnAlumnoCurso(idAlumno, idCurso):
    if not ConsultasInscripciones.existeAluEnAluCurso(idAlumno, idCurso):
        raise MisExceptions('No se ha encontrado un alumno con ese nombre y apellidos en ese curso')


def existeAlumnoEnAlumnoCurso(idAlumno, idCurso):
    if ConsultasInscripciones.existeAluEnAluCurso(idAlumno, idCurso):
        raise MisExceptions('Ese alumno ya esta matriculado en ese curso')


def noExisteProfesorEnCurso(idProfesor, idCurso):
    if not ConsultasInscripciones.existeProfEnCurso(idProfesor, idCurso):
        raise MisExceptions('No se ha encontrado un profesor con ese dni en ese curso')


def existeProfesorEnCurso(idProfesor, idCurso):
    if ConsultasInscripciones.existeProfEnCurso(idProfesor, idCurso):
        raise MisExceptions('Ese profesor ya esta matriculado en ese curso')
