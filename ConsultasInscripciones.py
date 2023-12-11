import pymysql
from ConexionBBDD import conect


def matAlu(nomCurso, nomAlu, apeAlu):
    """
    Funcion para introducir los datos en la base de datos en la tabla de alumno_curso cuando matriculamos un alumno
    :param nomCurso: Recibe el nombre del curso
    :param nomAlu: Recibe el nombre del alumno
    :param apeAlu: Recibe el apellido del alumno
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT cod_curso FROM curso WHERE nombre = '{nomCurso}'")
        codCurso = cursor.fetchone()
        cursor.execute(f"SELECT num_expediente FROM alumno WHERE nombre = '{nomAlu}' AND apellidos = '{apeAlu}'")
        codAlu = cursor.fetchone()

        if codCurso and codAlu:
            codCurso = codCurso[0]
            codAlu = codAlu[0]
            cursor.execute(f"INSERT INTO alumno_curso (num_exp_alu, cod_curso) VALUES ({codAlu},{codCurso})")
            con.commit()

        cursor.close()


    except pymysql.Error as err:
        print(err)


def asigProf(nomCurso, dniProf):
    """
    Funcion para introducir la id del profesor en la tabla de curso al que queremos asignarle
    :param nomCurso: Recibe el nombre del curso
    :param dniProf: Recibe el dni del profesor
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT cod_curso FROM curso WHERE nombre = '{nomCurso}'")
        codCurso = cursor.fetchone()
        cursor.execute(f"SELECT id FROM profesor WHERE dni = '{dniProf}'")
        codProf = cursor.fetchone()

        if codCurso and codProf:
            codProf = codProf[0]
            codCurso = codCurso[0]
            cursor.execute(f"UPDATE curso SET id_profesor = {codProf} WHERE cod_curso = {codCurso}")
            con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)


def obtIdProf(dni):
    """
    Funcion para obtener la id del profesor
    :param dni: Recibe el dni del profesor
    :return: Retorna la id del profesor
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT id FROM profesor WHERE dni = '{dni}'")
        idProf = cursor.fetchone()
        cursor.close()
        if idProf:
            idProf = idProf[0]
            return idProf
    except pymysql.Error as err:
        print(err)


def obtIdAlu(nomAlu, apeAlu):
    """
    Funcino para obtener la id del alumno
    :param nomAlu: Recibe el nombre del alumno
    :param apeAlu: Recibe el apellido del alumno
    :return: Retorna la id del alumno
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT num_expediente FROM alumno WHERE nombre = '{nomAlu}' AND apellidos = '{apeAlu}'")
        idAlu = cursor.fetchone()
        cursor.close()
        if idAlu:
            idAlu = idAlu[0]
            return idAlu
    except pymysql.Error as err:
        print(err)


def obtIdCurso(nombre):
    """
    Funcion para obtener la id de un curso
    :param nombre: Recibe el nombre del curso
    :return: Retorna la id del profesor
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT cod_curso FROM curso WHERE nombre = '{nombre}'")
        idCurso = cursor.fetchone()
        cursor.close()
        if idCurso:
            idCurso = idCurso[0]
            return idCurso
    except pymysql.Error as err:
        print(err)


def borrarAluCurso(idAlu, idCurso):
    """
    Funcion para borrar un el alumno de la tabla de alumno_curso
    :param idAlu: Recibe la id del alumno
    :param idCurso: Recibe la id del curso
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM alumno_curso WHERE num_exp_alu = {idAlu} AND cod_curso = {idCurso}")
        print("Alumno desmatriculado correctamente")
        con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)


def borrarProfCurso(idProfe, idCurso):
    """
    Funcion para actualizar la tabla de curso y eliminar al profesor de ese curso
    :param idProfe: Recibe la id del profesor
    :param idCurso: Recibe la id del curso
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE curso SET id_profesor = NULL WHERE id_Profesor = {idProfe} AND cod_curso = {idCurso}")
        print("Profesor desmatriculado correctamente")
        con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)


def existeAluEnAluCurso(idAlu, idCurso):
    """
    Funcion para comprobar si existe o no el alumno en la tabla alumno_Curso
    :param idAlu: Recibe la id del alumno
    :param idCurso: Recibe la id del curso
    :return: Retorna si existe o no en la tabla
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT num_exp_alu FROM alumno_curso WHERE num_exp_alu = {idAlu} AND cod_curso = {idCurso}")
        existe = cursor.fetchone()
        cursor.close()
        if existe:
            return True

    except pymysql.Error as err:
        print(err)
        return False
    return False


def existeProfEnCurso(idProfe, idCurso):
    """
        Funcion para comprobar si existe o no el profesor en la tabla curso
        :param idProfe: Recibe la id del profesor
        :param idCurso: Recibe la id del curso
        :return: Retorna si existe o no en la tabla
        """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT id_profesor FROM curso WHERE id_profesor = {idProfe} AND cod_curso = {idCurso}")
        existe = cursor.fetchone()
        cursor.close()
        if existe:
            return True

    except pymysql.Error as err:
        print(err)
        return False
    return False


def hayAlumnosMatriculados():
    """
    Funcion que comprueba si hay alumnos matriculados en cursos
    :return: Retorna si lo hay o no
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM alumno_curso")
        resultados = cursor.fetchall()
        cursor.close()
        if resultados:
            return True
    except pymysql.Error as err:
        print(err)
    print('Aun no hay alumnos dados de alta en ningun curso')
    return False


def hayProfesoresAsignados():
    """
    Funcion que comprueba si hay profesores asignados en cursos
    :return: Retorna si lo hay o no
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM curso")
        resultados = cursor.fetchall()
        cursor.close()
        for lines in resultados:
            if (lines[1] is not None):
                return True
    except pymysql.Error as err:
        print(err)
    print('Aun no hay profesores dados de alta en ningun curso')
    return False