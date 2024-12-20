import VerificationExceptions
import ConsultasProfesor
from prettytable import PrettyTable
from Utiles import *


def menu():
    """
    Funcion de menu de gestion de Profesor
    :return:
    """
    finMenuProfesores = False
    while not finMenuProfesores:
        opcion = input("\n\n\t[==== MENU PROFESORES ====>\n"
                       "\t[1. Alta\n"
                       "\t[2. Baja\n"
                       "\t[3. Modificar\n"
                       "\t[4. Consultar\n"
                       "\t[5. Mostrar Todos\n"
                       "\t[0. Salir\n"
                       "\t[===== Opcion: ")
        if opcion == "1":
            alta()
        elif opcion == "2":
            if ConsultasProfesor.hayProfesores():
                baja()
        elif opcion == "3":
            if ConsultasProfesor.hayProfesores():
                modificar()
        elif opcion == "4":
            if ConsultasProfesor.hayProfesores():
                consultar()
        elif opcion == "5":
            if ConsultasProfesor.hayProfesores():
                mostrarTodos()
        elif opcion == "0":
            print("Saliendo...")
            finMenuProfesores = True
        else:
            rojo("Entrada no valida")


def alta():
    """
    Funcion de alta que agrega un profesor
    :return:
    """
    dni = None
    nombre = None
    direccion = None
    telefono = None
    intentos = 0
    opcSalir = None
    salir = False
    while (intentos < 5 and salir is False):
        try:
            if (dni is None and opcSalir != '0'):
                aux = input('Introduce el dni del profesor o 0 para salir:\n').upper()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.dniFormat(aux)
                    VerificationExceptions.existDni(aux)
                    verde("DNI introducido correctamente")
                    dni = aux
                    intentos = 0
            if (nombre is None and opcSalir != '0'):
                aux = input('Introduce el nombre del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    verde("Nombre introducido correctamente")
                    nombre = aux
                    intentos = 0
            if (direccion is None and opcSalir != '0'):
                aux = input('Introduce la direccion del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    verde("Direccion introducida correctamente")
                    direccion = aux
                    intentos = 0
            if (telefono is None and opcSalir != '0'):
                aux = input('Introduce el telefeno del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.validar_telefono(aux)
                    verde("Telefono introducido correctamente")
                    telefono = aux
                    intentos = 0
                    salir = True
            if (opcSalir == '0'):
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            rojo(str(err))

    if (intentos < 5 and opcSalir != '0'):
        ConsultasProfesor.consAlta(dni, nombre, direccion, telefono)
    elif (opcSalir == '0'):
        print("Saliendo")
    else:
        amarillo("Se han superado el maximo de errores.")


def baja():
    """
    Funcion que da de baja un profesor
    :return:
    """
    dni = None
    opcSalir = None
    fallos = 0
    salir = False
    while (opcSalir != '0' and fallos < 5 and not salir):
        try:
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:").upper()
            opcSalir = aux
            if (opcSalir != '0'):
                VerificationExceptions.dniFormat(aux)
                VerificationExceptions.noExistDni(aux)
                dni = aux
                salir = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            rojo(str(err))
    if (fallos < 5 and opcSalir != '0'):
        salir = False
        while not salir:
            op = input("Seguro que quiere dar de baja al profesor?[S/N]").lower()
            if op == "s":
                ConsultasProfesor.consBaja(dni)
                salir = True
            elif op == "n":
                salir = True
                print("Saliendo sin guardar...")
            else:
                rojo("Entrada no valida.")
    elif (fallos == 5):
        amarillo("Has superado el maximos de fallos permitidos que son 5")
    else:
        print("Saliendo...")


def consultar():
    """
    Funcion que pide un dni de un profesor y muestra todos los datos del profesor
    :return:
    """
    dni = None
    opcSalir = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        entrar = True
        try:
            aux = input("\nIntroduzca el dni del profesor que quiera buscar o 0 pulsa para salir:").upper()
            opcSalir = aux
            if (opcSalir != '0'):
                VerificationExceptions.dniFormat(aux)
                VerificationExceptions.noExistDni(aux)
                dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            entrar = False
            rojo(str(err))
        if (fallos < 5 and opcSalir != '0' and entrar):
            profesor = ConsultasProfesor.consBusqueda(dni)
            x = PrettyTable()
            x.field_names = ["Id", "DNI", "Nombre", "Direccion", "Telefono", "Cursos"]
            for dato in profesor:
                x.add_row([dato.id, dato.dni, dato.nombre, dato.direccion, dato.telefono, siNone(dato.nombre_curso)])

            print()
            azul(str(x))
        elif (fallos == 5):
            amarillo("Has superado el maximos de fallos permitidos que son 5")
        elif (opcSalir == '0'):
            print("Saliendo...")


def modificar():
    """
    Funcion que mustra un menu para que elijas que quieres modificar y modificarlo
    :return:
    """
    dni = None
    opcSalir = None
    fallos = 0
    while (dni is None and opcSalir != '0' and fallos < 5):
        try:
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:").upper()
            opcSalir = aux
            if (opcSalir != '0'):
                VerificationExceptions.dniFormat(aux)
                VerificationExceptions.noExistDni(aux)
                dni = aux
            else:
                print("Saliendo...")
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            rojo(str(err))
    salir = False
    while (fallos < 5 and not salir and opcSalir != '0'):
        opc = input("\n\t[====== MODIFICACION PROFESOR ======\n"
                    "\t[1.DNI\n"
                    "\t[2.Nombre\n"
                    "\t[3.Direccion\n"
                    "\t[4.Telefono\n"
                    "\t[0.Salir\n"
                    "\t[Opcion: ")
        if opc == '1':
            nuevoDni = None
            fallos = 0
            opcSalir = None
            while (fallos < 5 and nuevoDni is None and opcSalir != '0'):
                try:
                    aux = input('Escriba el nuevo dni o pulse 0 para salir:').upper()
                    opcSalir = aux
                    if (opcSalir != '0'):
                        VerificationExceptions.dniFormat(aux)
                        VerificationExceptions.existDni(aux)
                        verde("DNI introducido correctamente")
                        nuevoDni = aux
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el dni del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'dni', nuevoDni)
                        verde("Modificacion realizada correctamente")
                        dni = nuevoDni
                    elif op == "n":
                        salir = True
                        print("Saliendo sin guardar...")
                    else:
                        rojo("Entrada no valida.")
            elif (fallos == 5):
                amarillo("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")


        elif opc == '2':
            nuevoNombre = None
            fallos = 0
            opcSalir = None
            while (fallos < 5 and nuevoNombre is None and opcSalir != '0'):
                try:
                    aux = input('Escriba el nuevo nombre o pulse 0 para salir:')
                    opcSalir = aux
                    if (opcSalir != '0'):
                        VerificationExceptions.hayAlgo(aux)
                        verde("Nombre introducido correctamente")
                        nuevoNombre = aux
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el nombre del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'nombre', nuevoNombre)
                        verde("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        rojo("Entrada no valida.")
            elif (fallos == 5):
                amarillo("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")

        elif opc == '3':
            nuevoDirec = None
            fallos = 0
            opcSalir = None
            while (fallos < 5 and nuevoDirec is None and opcSalir != '0'):
                try:
                    aux = input('Escriba la nueva direccion o pulse 0 para salir:')
                    opcSalir = aux
                    if (opcSalir != '0'):
                        VerificationExceptions.hayAlgo(aux)
                        verde("Direccion introducida correctamente")
                        nuevoDirec = aux
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar la direccion del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'direccion', nuevoDirec)
                        verde("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        rojo("Entrada no valida.")
            elif (fallos == 5):
                amarillo("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")

        elif opc == '4':
            nuevoTel = None
            fallos = 0
            opcSalir = None
            while (fallos < 5 and nuevoTel is None and opcSalir != '0'):
                try:
                    aux = input('Escriba el nuevo telefono o pulse 0 para salir:')
                    opcSalir = aux
                    if (opcSalir != '0'):
                        VerificationExceptions.validar_telefono(aux)
                        verde("Telefeno introducido correctamente")
                        nuevoTel = aux
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el telefono del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'telefono', nuevoTel)
                        verde("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        rojo("Entrada no valida.")
            elif (fallos == 5):
                amarillo("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")

        elif opc == '0':
            print("Saliendo...")
            salir = True
        else:
            rojo("No hay esa opcion")


def mostrarTodos():
    """
    Funcion que muestra todos los profesores
    :return:
    """
    tabla = ConsultasProfesor.mostrarTabla()
    x = PrettyTable()
    x.field_names = ["Id", "DNI", "Nombre", "Direccion", "Telefono", "Cursos"]
    for dato in tabla:
        x.add_row([dato.id, dato.dni, dato.nombre, dato.direccion, dato.telefono, siNone(dato.nombre_curso)])

    print()
    azul(str(x))
