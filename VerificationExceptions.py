from datetime import datetime


class MisExceptions(Exception):
    def __init__(self, message="Error"):
        self.message = message

        super().__init__(self.message)


def hayAlgo(cadena):
    if (len(cadena) == 0):
        raise MisExceptions('No se ha escrito nada')


def dniFormat(dni):
    if len(dni) != 9:
        raise MisExceptions('Debe tener 9 caractres')
    if not dni[:-1].isdigit():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')
    if not dni[-1].isalpha():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')



def esNum(num):
    if type(num) != int:
        raise MisExceptions('Debe introducir solo numeros')


def formatoFecha(fecha):
    formato = "%Y-%m-%d"
    try:
        datetime.strptime(fecha, formato)
    except ValueError:
        raise MisExceptions('Formato de la fecha incorrecto. Formato esperado yyyy-mm-dd')