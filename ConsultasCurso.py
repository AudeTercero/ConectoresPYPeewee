from Tablas_BBDD import *
from peewee import *
from Utiles import *

def consAlta(nombre, descripcion):
    """
    Introduce un curso en la tabla de cursos
    :param nombre: El nombre del curso
    :param descripcion: La descripcion del curso
    :return:
    """
    Curso.create(nombre=nombre, descripcion=descripcion)


def consBaja(nombre):
    """
    Da de baja un curso
    :param nombre: EL curso que se busca
    :return:
    """
    Curso.select().where(Curso.nombre == nombre).get().delete_instance()


def consBusqueda(nombre):
    """
    Consulta un curso concreto y recibe
    sus datos, su profesor y sus alumnos
    :param nombre: El nombre que se busca
    :return: Devuelve los datos de ese curso
    """
    query = (Curso
             .select(Curso, fn.CONCAT(Profesor.nombre).alias('nombre_profesor'),
                     fn.GROUP_CONCAT(Alumno.nombre, ' ', Alumno.apellidos).alias('alumnos'))
             .left_outer_join(Profesor, on=(Curso.id_profesor_id == Profesor.id))
             .left_outer_join(AlumnoCurso, on=(Curso.cod_curso == AlumnoCurso.cod_curso_id))
             .left_outer_join(Alumno, on=(AlumnoCurso.num_exp_alu_id == Alumno.num_expediente))
             .where(Curso.nombre == nombre)
             .group_by(Curso.cod_curso))
    return query


def mostrarTabla():
    """
    Consulta todos los cursos de la tabla alumnos
    :return: Devuelve todos los cursos
    """
    query = (Curso
             .select(Curso, fn.CONCAT(Profesor.nombre).alias('nombre_profesor'),
                     fn.GROUP_CONCAT(Alumno.nombre, ' ', Alumno.apellidos).alias('alumnos'))
             .left_outer_join(Profesor, on=(Curso.id_profesor_id == Profesor.id))
             .left_outer_join(AlumnoCurso, on=(Curso.cod_curso == AlumnoCurso.cod_curso_id))
             .left_outer_join(Alumno, on=(AlumnoCurso.num_exp_alu_id == Alumno.num_expediente))
             .group_by(Curso.cod_curso))
    return query


def consModificar(nombre, columna, nuevoCampo):
    """
    Modifica el valor de un campo concreto en un curso buscado
    :param nombre: El nombre del curso que se busca
    :param columna: La columna que se quiere modificar
    :param nuevoCampo: El nuevo valor que tendra esa columna
    :return:
    """
    Curso.update({columna: nuevoCampo}).where(Curso.nombre == nombre).execute()


def existeCurso(nombre):
    """
    Comprueba en la tabla cursos que exista un curso con el nombre recibido
    :param nombre: El nombre que se busca
    :return: Devuelve true o false si lo encuentra o no
    """
    query = Curso.select().where(Curso.nombre == nombre)
    if query.count() > 0:
        return True
    else:
        return False


def hayCursos():
    """
    Comprueba que haya cursos registrados en la base de datos
    :return: True o False dependiendo de si hay o no
    """
    query = Curso.select()
    if query.count() > 0:
        return True
    else:
        amarillo('\nAun no hay cursos dados de alta')
        return False
