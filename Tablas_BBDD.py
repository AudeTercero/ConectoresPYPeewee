from peewee import *
from ConexionBBDD import conect


class Profesor(Model):
    """
    Clase Profesor para crear la tabla con los datos del profesor
    """
    id = AutoField(primary_key=True)
    dni = CharField(null=False, max_length=9, unique=True, constraints=[Check("dni REGEXP '^[0-9]{8}[A-Za-z]$'")])
    nombre = CharField(null=False, max_length=20)
    direccion = CharField(null=False, max_length=35)
    telefono = CharField(null=False, max_length=9)

    class Meta:
        database = conect()


class Alumno(Model):
    """
    Clase Alumno para crear la tabla con los datos del alumno
    """
    num_expediente = AutoField(primary_key=True)
    nombre = CharField(null=False, max_length=20)
    apellidos = CharField(null=False, max_length=35)
    telefono = CharField(null=False, max_length=9)
    direccion = CharField(null=False, max_length=35)
    fecha_nacimiento = DateField(null=False, formats=['%Y-%m-%d'])

    class Meta:
        unique_together = ('nombre', 'apellidos')
        database = conect()


class Curso(Model):
    """
    Clase Curso para crear la tabla con los datos del curso
    """
    cod_curso = AutoField(primary_key=True)
    id_profesor = ForeignKeyField(Profesor, field="id", null=True, on_update="SET NULL", on_delete="SET NULL")
    nombre = CharField(null=False, max_length=20, unique=True)
    descripcion = TextField(null=False)

    class Meta:
        database = conect()


class AlumnoCurso(Model):
    """
    Clase AlumnoCurso para crear la tabla de alumnocurso con los datos de la matriculacion del alumno al curso
    """
    num_exp_alu = ForeignKeyField(Alumno, field="num_expediente", null=False, on_update="CASCADE", on_delete="CASCADE")
    cod_curso = ForeignKeyField(Curso, field="cod_curso", null=False, on_update="CASCADE", on_delete="CASCADE")

    class Meta:
        primary_key = CompositeKey('num_exp_alu', 'cod_curso')
        database = conect()


def crear_tabla():
    """
    Funcion para crear las tablas
    """
    bd = conect()
    bd.connect()
    bd.create_tables([Alumno,Profesor,Curso,AlumnoCurso])
    bd.close()

