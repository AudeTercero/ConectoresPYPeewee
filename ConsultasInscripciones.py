from Tablas_BBDD import *


def matAlu(nomCurso, nomAlu, apeAlu):
    """
    Funcion para introducir los datos en la base de datos en la tabla de alumno_curso cuando matriculamos un alumno
    :param nomCurso: Recibe el nombre del curso
    :param nomAlu: Recibe el nombre del alumno
    :param apeAlu: Recibe el apellido del alumno
    :return:
    """
    curso = Curso.select().where(Curso.nombre == nomCurso).first()
    id_curso = curso.cod_curso
    alumno = Alumno.select().where((Alumno.nombre == nomAlu) and (Alumno.apellidos == apeAlu)).first()
    id_alumno = alumno.num_expediente
    print(id_curso, id_alumno)
    AlumnoCurso.create(cod_curso_id=id_curso, num_exp_alu_id=id_alumno)


def asigProf(nomCurso, dniProf):
    """
    Funcion para introducir la id del profesor en la tabla de curso al que queremos asignarle
    :param nomCurso: Recibe el nombre del curso
    :param dniProf: Recibe el dni del profesor
    :return:
    """
    curso = Curso.select().where(Curso.nombre == nomCurso).first()
    id_curso = curso.cod_curso
    profesor = Profesor.select().where(Profesor.dni == dniProf).first()
    id_profe = profesor.id
    Curso.update(id_profesor=id_profe).where(Curso.cod_curso == id_curso).execute()


def obtIdProf(dni):
    """
    Funcion para obtener la id del profesor
    :param dni: Recibe el dni del profesor
    :return: Retorna la id del profesor
    """
    profe = Profesor.select().where(Profesor.dni == dni).first()
    return profe.id


def obtIdAlu(nomAlu, apeAlu):
    """
    Funcino para obtener la id del alumno
    :param nomAlu: Recibe el nombre del alumno
    :param apeAlu: Recibe el apellido del alumno
    :return: Retorna la id del alumno
    """
    alumno = Alumno.select().where(Alumno.nombre == nomAlu and Alumno.apellidos == apeAlu).first()
    return alumno.num_expediente


def obtIdCurso(nombre):
    """
    Funcion para obtener la id de un curso
    :param nombre: Recibe el nombre del curso
    :return: Retorna la id del profesor
    """
    curso = Curso.select().where(Curso.nombre == nombre).first()
    return curso.cod_curso


def borrarAluCurso(idAlu, idCurso):
    """
    Funcion para borrar un el alumno de la tabla de alumno_curso
    :param idAlu: Recibe la id del alumno
    :param idCurso: Recibe la id del curso
    :return:
    """
    AlumnoCurso.delete().where(AlumnoCurso.num_exp_alu == idAlu and AlumnoCurso.cod_curso == idCurso).execute()
    print("Alumno desmatriculado correctamente")


def borrarProfCurso(idProfe, idCurso):
    """
    Funcion para actualizar la tabla de curso y eliminar al profesor de ese curso
    :param idProfe: Recibe la id del profesor
    :param idCurso: Recibe la id del curso
    :return:
    """
    Curso.update(id_profesor=None).where(Curso.cod_curso == idCurso and Curso.id_profesor == idProfe).execute()
    print("Profesor desmatriculado correctamente")


def existeAluEnAluCurso(idAlu, idCurso):
    """
    Funcion para comprobar si existe o no el alumno en la tabla alumno_Curso
    :param idAlu: Recibe la id del alumno
    :param idCurso: Recibe la id del curso
    :return: Retorna si existe o no en la tabla
    """
    alumno = AlumnoCurso.select().where(AlumnoCurso.num_exp_alu_id == idAlu and AlumnoCurso.cod_curso_id == idCurso)
    return alumno.exists()


def existeProfEnCurso(idProfe, idCurso):
    """
        Funcion para comprobar si existe o no el profesor en la tabla curso
        :param idProfe: Recibe la id del profesor
        :param idCurso: Recibe la id del curso
        :return: Retorna si existe o no en la tabla
        """
    curso = Curso.select().where(Curso.id_profesor_id == idProfe and Curso.cod_curso == idCurso)
    return curso.exists()


def hayAlumnosMatriculados():
    """
    Funcion que comprueba si hay alumnos matriculados en cursos
    :return: Retorna si lo hay o no
    """
    if AlumnoCurso.select().exists():
        return True
    else:
        print('Aun no hay alumnos dados de alta en ningun curso')
        return False


def hayProfesoresAsignados():
    """
    Funcion que comprueba si hay profesores asignados en cursos
    :return: Retorna si lo hay o no
    """
    cursos = Curso.select()
    for curso in cursos:
        if curso.id_profesor is not None:
            return True
    print('Aun no hay profesores dados de alta en ningun curso')
    return False


def tiene_profe(curso):
    '''
    Metodo para verificar si un curso tiene o no un profesor asignado
    :param curso: nombre del curso a comprobar
    :return:
    '''
    cursos = Curso.select().where(Curso.nombre == curso)
    for curso in cursos:
        if curso.id_profesor is not None:
            return True
    return False
