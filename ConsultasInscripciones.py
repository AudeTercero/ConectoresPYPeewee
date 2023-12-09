import pymysql
from ConexionBBDD import conect


def matAlu(nomCurso, nomAlu, apeAlu):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT cod_curso FROM curso WHERE nombre = '{nomCurso}'")
        codCurso = cursor.fetchone()
        cursor.execute(f"SELECT num_expediente FROM curso WHERE nombre = '{nomAlu}' AND apellidos = '{apeAlu}'")
        codAlu = cursor.fetchone()

        if codCurso and codAlu:
            codCurso = codCurso[0]
            codAlu = codAlu[0]
            cursor.execute(f"INSERT INTO alumno_curso (num_exp_alu, cod_curso) VALUES ({codCurso},{codAlu})")
            con.commit()

        cursor.close()


    except pymysql.Error as err:
        print(err)


def asigProf(nomCurso, dniProf):
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
            cursor.execute(f"UPEDATE curso SET id_profesor = {codProf} WHERE curso = {codCurso}")
            con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)


def obtIdProf(dni):
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
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT num_expediente FROM alumno WHERE nombre = '{nomAlu}' AND apellido = '{apeAlu}'")
        idAlu = cursor.fetchone()
        cursor.close()
        if idAlu:
            idAlu = idAlu[0]
            return idAlu
    except pymysql.Error as err:
        print(err)


def obtIdCurso(nombre):
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
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM alumno_curso WHERE num_exp_alu = {idAlu} AND cod_curso = {idCurso}")
        print("Alumno desmatriculado correctamente")
        cursor.close()
    except pymysql.Error as err:
        print(err)
def borrarProfCurso(idProfe, idCurso):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE curso SET id_profesor = '' WHERE id_Profesor = {idProfe} AND cod_curso = {idCurso}")
        print("Profesor desmatriculado correctamente")
        cursor.close()
    except pymysql.Error as err:
        print(err)

def existeAluEnAluCurso(idAlu, idCurso):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT num_exp_alu FROM alumno_curso WHERE num_exp_alu = {idAlu}, cod_curso = {idCurso}")
        existe = cursor.fetchone()
        cursor.close()
        if existe:
            return True

    except pymysql.Error as err:
        print(err)
        return False
    return False


def existeProfEnCurso(idProfe, idCurso):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT id_profesor FROM curso WHERE id_profesor = {idProfe}, cod_curso = {idCurso}")
        existe = cursor.fetchone()
        cursor.close()
        if existe:
            return True

    except pymysql.Error as err:
        print(err)
        return False
    return False
