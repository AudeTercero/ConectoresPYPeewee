import pymysql
from Tablas_BBDD import Alumno, AlumnoCurso, Curso
from peewee import *


def consAlta(nombre, apellidos, telefono, direccion, fecha):
    try:
        Alumno.create(nombre=nombre, apellidos=apellidos, telefono=telefono, direccion=direccion,
                      fecha_nacimiento=fecha)
        print("Alumno creado correctamente")
    except Exception as e:
        print(f"Error al guardar alumno en la base de datos: {e}")


def consBaja(nombre, apellidos):
    try:
        Alumno.delete().where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos)).execute()
        print("Alumno dado de baja correctamente")
    except pymysql.Error as err:
        print(err)


def consModificar(nombre, apellidos, columna, nuevoCampo):
    Alumno.update({columna: nuevoCampo}).where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos)).execute()


def consBuscar(nombre, apellidos):
    try:
        resultados = (Alumno
                      .select(Alumno, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_cursos'))
                      .left_outer_join(AlumnoCurso, on=(Alumno.num_expediente == AlumnoCurso.num_exp_alu_id))
                      .left_outer_join(Curso, on=(AlumnoCurso.cod_curso_id == Curso.cod_curso))
                      .where((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos))
                      .group_by(Alumno.num_expediente))

        return resultados
    except Exception as e:
        print(f"Error al buscar alumno: {e}")


def consMostrarAlumnos():
    try:
        resultados = (Alumno
                      .select(Alumno, fn.GROUP_CONCAT(Curso.nombre).alias('nombre_cursos'))
                      .left_outer_join(AlumnoCurso, on=(Alumno.num_expediente == AlumnoCurso.num_exp_alu_id))
                      .left_outer_join(Curso, on=(AlumnoCurso.cod_curso_id == Curso.cod_curso))
                      .group_by(Alumno.num_expediente))

        return resultados
    except Exception as e:
        print(f"Error al mostrar alumnos: {e}")


def existeAlumno(nombre, apellidos):
    try:
        alumno = Alumno.get((Alumno.nombre == nombre) & (Alumno.apellidos == apellidos))
        return True
    except DoesNotExist:
        return False
    except Exception as e:
        print(f"Error al buscar alumno: {e}")
        return False


def hayAlumnos():
    try:
        total_alumnos = Alumno.select().count()

        if total_alumnos > 0:
            return True
        else:
            print('\nAun no hay alumnos dados de alta')
            return False
    except Exception as e:
        print(f"Error al verificar la existencia de alumnos: {e}")
        return False
