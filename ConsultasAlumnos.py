import pymysql
from Tablas_BBDD import Alumno, AlumnoCurso, Curso
from peewee import *


def consAlta(nombre, apellidos, telefono, direccion, fecha):
    Alumno.create(nombre=nombre, apellidos=apellidos, telefono=telefono, direccion=direccion,
                  fecha_nacimiento=fecha)
    print("Alumno creado correctamente")


def consBaja(nombre, apellidos):
    Alumno.delete().where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos)).execute()
    print("Alumno dado de baja correctamente")


def consModificar(nombre, apellidos, columna, nuevoCampo):
    Alumno.update({columna: nuevoCampo}).where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos)).execute()


def consBuscar(nombre, apellidos):
    resultados = (Alumno
                  .select(Alumno, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_cursos'))
                  .left_outer_join(AlumnoCurso, on=(Alumno.num_expediente == AlumnoCurso.num_exp_alu_id))
                  .left_outer_join(Curso, on=(AlumnoCurso.cod_curso_id == Curso.cod_curso))
                  .where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos))
                  .group_by(Alumno.num_expediente))

    return resultados


def consMostrarAlumnos():
    resultados = (Alumno
                  .select(Alumno, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_cursos'))
                  .left_outer_join(AlumnoCurso, on=(Alumno.num_expediente == AlumnoCurso.num_exp_alu_id))
                  .left_outer_join(Curso, on=(AlumnoCurso.cod_curso_id == Curso.cod_curso))
                  .group_by(Alumno.num_expediente))

    return resultados


def existeAlumno(nombre, apellidos):
    query = Alumno.select().where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos))
    if query.count() > 0:
        return True
    else:
        return False


def hayAlumnos():
    total_alumnos = Alumno.select().count()

    if total_alumnos > 0:
        return True
    else:
        print('\nAun no hay alumnos dados de alta')
        return False
