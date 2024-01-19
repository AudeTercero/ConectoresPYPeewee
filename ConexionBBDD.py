import pymysql
from peewee import *

def conect():
    """
    Funcion que crea la base de datos si no existe y hace la conexion con ella
    :return:Retorna la conexion
    """
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
        db = MySQLDatabase('Marcos_Javier_Iker', user=prop['user'], password=prop['password'], host=prop['host'],
                           port=int(prop['port']))

        return db

    except pymysql.Error and Exception as err:
        # print(f"Error de conexión a la base de datos: {err}")
        return None


def leerConf():
    """
    Funcion que lee el documento de propiedadas de la base de datos
    :return: Retorna una coleccion con los datos ordenados por clave valor
    """
    propiedades = {}
    with open('conf.prop', 'r') as file:
        for linea in file:
            key, value = linea.strip().split('=')
            propiedades[key] = value

    return propiedades
