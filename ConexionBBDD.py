import pymysql


def conexion():
    con = conect()
    cursor = con.cursor()
    with open('Marcos_Javier_IkerBBDD.sql', 'r') as file:
        sql_commands = file.read()
        comandos = sql_commands.split(";")
        for comando in comandos:
            if comando.strip():
                cursor.execute(comando)
    con.commit()



def conect():
    try:
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='alumno',
            database='',
            port=3307
        )
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Marcos_Javier_Iker;")
        con.commit()
        cursor.close()
        con.close()

        con = pymysql.connect(
            host='localhost',
            user='root',
            password='alumno',
            database='Marcos_Javier_Iker',
            port=3307
        )
        return con

    except pymysql.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
def leerConf():
    with open('conf.prop','r') as file:
        propiedades = file.read()
