import pymysql
from ConexionBBDD import conect

def consAlta(nombre, apellidos, telefono, direccion, fecha):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"INSERT INTO alumno (nombre,apellidos,telefono,direccion,fecha) VALUES ('{nombre}','{apellidos}','{telefono}','{direccion}','{fecha}')")
        conect.commit()
        cursor.close()
        print("Alumno guardado correctamente")
    except pymysql.Error as err:
        print(err)

def consBaja(nombre, apellidos):
    try:
        cursor = conect.cursor()
        cursor.execute(
            f"DELETE FROM alumno WHERE nombre = '{nombre}' AND apellidos = '{apellidos}'")
        conect.commit()
        cursor.close()
        print("Alumno dado de baja correctamente")
    except pymysql.Error as err:
        print(err)

def consModificar(nombre, apellidos, columna, nuevoCampo):
    try:
        cursor = conect.cursor()
        cursor.execute(f"UPDATE alumno SET {columna} = '{nuevoCampo}' WHERE nombre = '{nombre}' AND apellidos = '{apellidos}'")
        resultados = cursor.fetchall()
        conect.commit()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)

def consBuscar(nombre, apellidos):
    print()

def consMostrarAlumnos():
    print()

def existeAlumno(nombre, apellidos):
    print()