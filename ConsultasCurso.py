import pymysql
from ConexionBBDD import conect


def consAlta(nombre, descripcion):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO curso (nombre,descripcion) VALUES ('{nombre}','{descripcion}')")
        con.commit()
        cursor.close()
        print("Curso guardado correctamente")
    except pymysql.Error as err:
        print(err)


def consBaja(nombre):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"DELETE FROM curso WHERE nombre = '{nombre}'")
        con.commit()
        cursor.close()
        print("Curso dado de baja correctamente")
    except pymysql.Error as err:
        print(err)


def consBusqueda(nombre):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute("""
            SELECT 
                c.cod_curso,
                c.nombre AS nombre_curso,
                a.num_expediente,
                a.nombre AS nombre_alumno,
                a.apellidos,
                p.nombre AS nombre_profesor
            FROM 
                curso c
            LEFT JOIN 
                alumno_curso ac ON c.cod_curso = ac.cod_curso
            LEFT JOIN 
                alumno a ON ac.num_exp_alu = a.num_expediente
            LEFT JOIN 
                profesor p ON c.id_profesor = p.id
            WHERE 
                c.nombre = '{nombre_curso}'
        """)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def mostrarTabla():
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM curso")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def existeCurso(nombre):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT nombre FROM curso WHERE nombre = '{nombre}'")
        resultados = cursor.fetchall()
        cursor.close()
        if len(resultados) and resultados[0][0] == nombre:
            return True
    except pymysql.Error as err:
        print(err)

    return False


def consModificar(nombre, columna, nuevoCampo):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE curso SET {columna} = '{nuevoCampo}' WHERE nombre = '{nombre}'")
        resultados = cursor.fetchall()
        con.commit()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)
