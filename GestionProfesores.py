import VerificationExceptions
import ConsultasProfesor


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
            print("Entrada no valida")


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
                    print("DNI introducido correctamente")
                    dni = aux
                    intentos = 0
            if (nombre is None and opcSalir != '0'):
                aux = input('Introduce el nombre del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    print("Nombre introducido correctamente")
                    nombre = aux
                    intentos = 0
            if (direccion is None and opcSalir != '0'):
                aux = input('Introduce la direccion del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    print("Direccion introducida correctamente")
                    direccion = aux
                    intentos = 0
            if (telefono is None and opcSalir != '0'):
                aux = input('Introduce el telefeno del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.validar_telefono(aux)
                    print("Telefono introducido correctamente")
                    telefono = aux
                    intentos = 0
                    salir = True
            if (opcSalir == '0'):
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)

    if (intentos < 5 and opcSalir != '0'):
        ConsultasProfesor.consAlta(dni, nombre, direccion, telefono)
    elif (opcSalir == '0'):
        print("Saliendo")
    else:
        print("Se han superado el maximo de errores.")


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
            print(err)
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
                print("Entrada no valida.")
    elif (fallos == 5):
        print("Has superado el maximos de fallos permitidos que son 5")
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
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:").upper()
            opcSalir = aux
            if (opcSalir != '0'):
                VerificationExceptions.dniFormat(aux)
                VerificationExceptions.noExistDni(aux)
                dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            entrar = False
            print(err)
        if (fallos < 5 and opcSalir != '0' and entrar):
            profesor = ConsultasProfesor.consBusqueda(dni)
            for tupla in profesor:
                print(f'''---Profesor---
Id: {tupla[0]}, DNI: {tupla[1]}, Nombre: {tupla[2]}, Direccion: {tupla[3]}, Telefono: {tupla[4]}, Cursos: {tupla[5]}''')
        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
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
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    salir = False
    while (fallos < 5 and not salir):
        opc = input(''' 
                    ******* MODIFICACION PROFESOR *******
                    1.DNI
                    2.Nombre
                    3.Direccion
                    4.Telefono
                    0.Salir
                    ''')
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
                        print("DNI introducido correctamente")
                        nuevoDni = aux
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el dni del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'dni', nuevoDni)
                        print("Modificacion realizada correctamente")
                        dni = nuevoDni
                    elif op == "n":
                        salir = True
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif (fallos == 5):
                print("No puedes fallar mas de 5 veces")

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
                        print("Nombre introducido correctamente")
                        nuevoNombre = aux
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el nombre del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'nombre', nuevoNombre)
                        print("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif (fallos == 5):
                print("No puedes fallar mas de 5 veces")

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
                        print("Direccion introducida correctamente")
                        nuevoDirec = aux
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar la direccion del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'direccion', nuevoDirec)
                        print("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif (fallos == 5):
                print("No puedes fallar mas de 5 veces")

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
                        print("Telefeno introducido correctamente")
                        nuevoTel = aux
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if (fallos < 5 and opcSalir != '0'):
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el telefono del profesor?[S/N]").lower()
                    if op == "s":
                        ConsultasProfesor.consModificar(dni, 'telefono', nuevoTel)
                        print("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True;
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif (fallos == 5):
                print("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")

        elif opc == '0':
            print("Saliendo...")
            salir = True
        else:
            print("No hay esa opcion")


def mostrarTodos():
    """
    Funcion que muestra todos los profesores
    :return:
    """
    tabla = ConsultasProfesor.mostrarTabla()
    print("\n\n\t\t[==== PROFESORES ====>")
    for dato in tabla:
        print(f"\t\t[ID: {dato[0]}  -DNI: {dato[1]}  -Nombre: {dato[2]}  -Direccion: {dato[3]}  -Telefono: {dato[4]}\n"
              f"\t\t[\t -Cursos: {dato[5]}")
    print("\t\t[====================>")
