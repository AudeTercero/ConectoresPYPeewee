from peewee import *
from ConexionBBDD import conect


class Profesor(Model):
    id = AutoField(primary_key=True)
    dni = CharField(null=False, max_length=9, unique=True, constraints=[Check("dni REGEXP '^[0-9]{8}[A-Za-z]$'")])
    nombre = CharField(null=False, max_length=20)
    direccion = CharField(null=False, max_length=35)
    telefono = CharField(null=False, max_length=9)

    class Meta:
        database = conect()


class Alumno(Model):
    num_expediente = AutoField(primary_key=True)
    nombre = CharField(null=False, max_length=20)
    apellidos = CharField(null=False, max_length=35)
    telefono = CharField(null=False, max_length=9)
    direccion = CharField(null=False, max_length=35)
    fecha_nacimiento = DateField(null=False, constraints=[Check("fecha_nacimiento STR_TO_DATE(fecha_nacimiento, '%Y-%m-%d')")])

    class Meta:
        unique_together = ('nombre', 'apellidos')
        database = conect()


class Curso(Model):
    cod_curso = AutoField(primary_key=True)
    id_profesor = ForeignKeyField(Profesor, field="id", null=True, on_update="SET NULL", on_delete="SET NULL")
    nombre = CharField(null=False, max_length=20, unique=True)
    descripcion = TextField(null=False)

    class Meta:
        database = conect()


class AlumnoCurso(Model):
    num_exp_alu = ForeignKeyField(Alumno, field="num_expediente", null=False, on_update="CASCADE", on_delete="CASCADE")
    cod_curso = ForeignKeyField(Curso, field="cod_curso", null=False, on_update="CASCADE", on_delete="CASCADE")

    class Meta:
        primary_key = CompositeKey('num_exp_alu', 'cod_curso')
        database = conect()


def crear_tabla():
    bd = conect()
    bd.connect()
    bd.create_tables([Alumno,Profesor,Curso,AlumnoCurso])
    bd.close()

