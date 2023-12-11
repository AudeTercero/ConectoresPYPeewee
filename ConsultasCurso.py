import pymysql
from ConexionBBDD import conect


def consAlta(nombre, descripcion):
    """
    Introduce un curso en la tabla de cursos
    :param nombre: El nombre del curso
    :param descripcion: La descripcion del curso
    :return:
    """
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
    """
    Da de baja un curso
    :param nombre: EL curso que se busca
    :return:
    """
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
    """
    Consulta un curso concreto y recibe
    sus datos, su profesor y sus alumnos
    :param nombre: El nombre que se busca
    :return: Devuelve los datos de ese curso
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"""
            SELECT 
                c.cod_curso,
                c.nombre AS nombre_curso,
                c.descripcion,
                p.nombre AS nombre_profesor,
                GROUP_CONCAT(CONCAT(a.nombre, ' ', a.apellidos) SEPARATOR ', ') AS alumnos
            FROM 
                curso c
            LEFT JOIN 
                profesor p ON c.id_profesor = p.id
            LEFT JOIN 
                alumno_curso ac ON c.cod_curso = ac.cod_curso
            LEFT JOIN 
                alumno a ON ac.num_exp_alu = a.num_expediente
            WHERE 
                c.nombre = '{nombre}'
            GROUP BY 
                c.cod_curso
        """)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def mostrarTabla():
    """
    Consulta todos los cursos de la tabla alumnos
    :return: Devuelve todos los cursos
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"""
                    SELECT 
                        c.cod_curso,
                        c.nombre AS nombre_curso,
                        c.descripcion,
                        p.nombre AS nombre_profesor,
                        GROUP_CONCAT(CONCAT(a.nombre, ' ', a.apellidos) SEPARATOR ', ') AS alumnos
                    FROM 
                        curso c
                    LEFT JOIN 
                        profesor p ON c.id_profesor = p.id
                    LEFT JOIN 
                        alumno_curso ac ON c.cod_curso = ac.cod_curso
                    LEFT JOIN 
                        alumno a ON ac.num_exp_alu = a.num_expediente
                    GROUP BY 
                        c.cod_curso
                """)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except pymysql.Error as err:
        print(err)


def existeCurso(nombre):
    """
    Comprueba en la tabla cursos que exista un curso con el nombre recibido
    :param nombre: El nombre que se busca
    :return: Devuelve true o false si lo encuentra o no
    """
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
    """
    Modifica el valor de un campo concreto en un curso buscado
    :param nombre: El nombre del curso que se busca
    :param columna: La columna que se quiere modificar
    :param nuevoCampo: El nuevo valor que tendra esa columna
    :return:
    """
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"UPDATE curso SET {columna} = '{nuevoCampo}' WHERE nombre = '{nombre}'")
        con.commit()
        cursor.close()
    except pymysql.Error as err:
        print(err)

def hayCursos():
    con = conect()
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM curso")
        resultados = cursor.fetchall()
        cursor.close()
        if resultados:
            return True
    except pymysql.Error as err:
        print(err)
    print('\nAun no hay cursos dados de alta')
    return False
