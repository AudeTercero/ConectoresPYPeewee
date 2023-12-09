import pymysql
from ConexionBBDD import conect

def consAlta(nombre, apellidos, telefono, direccion, fecha):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO alumno (nombre,apellidos,telefono,direccion,fecha) VALUES ('{nombre}','{apellidos}','{telefono}','{direccion}','{fecha}')")
        con.commit()
        cursor.close()
        print("Alumno guardado correctamente")
    except pymysql.Error as err:
        print(err)

def consBaja(nombre, apellidos):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(
            f"DELETE FROM alumno WHERE nombre = '{nombre}' AND apellidos = '{apellidos}'")
        con.commit()
        cursor.close()
        print("Alumno dado de baja correctamente")
    except pymysql.Error as err:
        print(err)

def consModificar(nombre, apellidos, columna, nuevoCampo):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE alumno SET {columna} = '{nuevoCampo}' WHERE nombre = '{nombre}' AND apellidos = '{apellidos}'")
        resultados = cursor.fetchall()
        con.commit()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)

def consBuscar(nombre, apellidos):
    con = conect()
    try:
        cursor = con.connect()
        cursor.execute("SELECT a.*,c.nombre AS nombre_curso FROM alumno a "
                       "JOIN alumno_curso ON a.num_expediente = ac.num_exp_alu "
                       "JOIN curso c ON ac.cod_curso = c.cod_curso"
                       f"WHERE a.nombre = '{nombre}' AND a.apellidos = '{apellidos}'")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)

def consMostrarAlumnos():
    con = conect()
    try:
        cursor = con.connect()
        cursor.execute("SELECT a.*,c.nombre AS nombre_curso FROM alumno a "
                       "JOIN alumno_curso ON a.num_expediente = ac.num_exp_alu "
                       "JOIN curso c ON ac.cod_curso = c.cod_curso")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)

def existeAlumno(nombre, apellidos):
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT nombre, apellidos FROM alumno WHERE nombre = '{nombre}' AND apellidos = '{apellidos}'")
        resultados = cursor.fetchall()
        cursor.close()
        if (len(resultados) and resultados[0][0] == nombre and resultados [0][1] == apellidos):
            return True
    except pymysql.Error as err:
        print(err)
    return False