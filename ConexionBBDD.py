import pymysql


def conexion():
    cursor = None
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='alumno',
        database='',
        port=3307
    )
    try:
        cursor = con.cursor()
        cursor.execute("SHOW DATABASES LIKE 'Marcos_Javier_Iker';")
        existe_bbdd = cursor.fetchone()
        if not existe_bbdd:
            cursor.execute("CREATE DATABASE Marcos_Javier_Iker;")
    except pymysql.Error as err:
        print(err)
    finally:
        if 'con' in locals() and con.open:
            cursor.close()
            con.close()
    try:
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='alumno',
            database='Marcos_Javier_Iker',
            port=3307
        )
        cursor = con.cursor()

    except pymysql.Error as err:
        print(f"Error de conexión a la base de datos: {err}")

    with open('Marcos_Javier_IkerBBDD.sql', 'r') as file:
        sql_commands = file.read()
        comandos = sql_commands.split(";")
        for comando in comandos:
            if(comando.strip()):
                cursor.execute(comando)
    con.commit()



