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
    prop = leerConf()
    try:
        con = pymysql.connect(
            host=prop['host'],
            user=prop['user'],
            password=prop['password'],
            database='',
            port=int(prop['port'])
        )
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Marcos_Javier_Iker;")
        con.commit()
        cursor.close()
        con.close()

        con = pymysql.connect(
            host=prop['host'],
            user=prop['user'],
            password=prop['password'],
            database=prop['database'],
            port=int(prop['port'])
        )
        return con

    except pymysql.Error as err:
        print(f"Error de conexión a la base de datos: {err}")


def leerConf():
    propiedades = {}
    with open('conf.prop', 'r') as file:
        for linea in file:
            key, value = linea.strip().split('=')
            propiedades[key] = value

    return propiedades
