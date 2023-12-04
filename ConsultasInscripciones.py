import pymysql
from ConexionBBDD import conect





def matAlu(nomCurso, nomAlu, apeAlu):
    try:
        cursor = conect.cursor()
        cursor.execute(f"SELECT cod_curso FROM curso WHERE nombre = '{nomCurso}'")
        codCurso = cursor.fetchone()
        cursor.execute(f"SELECT num_expediente FROM curso WHERE nombre = '{nomAlu}' AND apellidos = '{apeAlu}'")
        codAlu = cursor.fetchone()


        if codCurso and codAlu:
            codCurso = codCurso[0]
            codAlu = codAlu[0]
            cursor.execute(f"INSERT INTO alumno_curso (num_exp_alu, cod_curso) VALUES ('{codCurso}','{codAlu}')")
            conect.commit()

        cursor.close()


    except pymysql.Error as err:
        print(err)


def existeCurso(nombre):
    try:
        cursor = conect.cursor()
        cursor.execute(f"SELECT nombre FROM curso WHERE nombre = '{nombre}'")
        resultados = cursor.fetchall()
        cursor.close()
        if (len(resultados) and resultados[0][0] == nombre):
            return True
    except pymysql.Error as err:
        print(err)

    return False
