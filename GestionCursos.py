import VerificationExceptions
import ConsultasCurso

def menu():
    finMenuCursos = False
    while not finMenuCursos:
        opcion = input("\n\n\t[==== MENU CURSOS ====>\n"
                       "\t[1. Alta\n"
                       "\t[2. Baja\n"
                       "\t[3. Modificar\n"
                       "\t[4. Consultar\n"
                       "\t[5. Mostrar Todos\n"
                       "\t[0. Salir\n"
                       "\t[===== Opcion: ")
        if opcion == "1":
            print("alta")
        elif opcion == "2":
            print("baja")
        elif opcion == "3":
            print("modificar")
        elif opcion == "4":
            print("consultar")
        elif opcion == "5":
            print("Mostrar todos")
        elif opcion == "0":
            print("Saliendo...")
            finMenuCursos = True
        else:
            print("Entrada no valida")


def alta():
    """
    Funcion de alta que agrega un profesor
    :return:
    """
    nombre = None
    descripcion = None
    intentos = 0
    opcSalir = None
    salir = False
    while intentos < 5 and salir is False:
        try:
            if nombre is None and opcSalir != '0':
                aux = input('Introduce el nombre del curso o 0 para salir:\n')
                opcSalir = aux
                if opcSalir != '0':
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    nombre = aux
                    intentos = 0
            if descripcion is None and opcSalir != '0':
                aux = input('Introduce la descripcion del curso o 0 para salir:\n')
                opcSalir = aux
                if opcSalir != '0':
                    VerificationExceptions.hayAlgo(aux)
                    descripcion = aux
                    intentos = 0
            if opcSalir == '0':
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)

    if intentos < 5 and opcSalir != '0':
        ConsultasCurso.consAlta(nombre, descripcion)
    elif opcSalir == '0':
        print("Saliendo")
    else:
        print("Se han superado el maximo de errores.")


def baja():
    """
    Funcion que da de baja un profesor
    :return:
    """
    nombre = None
    opcSalir = None
    fallos = 0
    while opcSalir != '0' and fallos < 5:
        try:
            aux = input("Introduzca el nombre del curso que quiera buscar o 0 pulsa para salir: ")
            opcSalir = aux
            if opcSalir != 0:
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.noExistNombreCur(aux)
                nombre = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if fallos < 5 and opcSalir != 0:
            salir = False
            while not salir:
                op = input("Seguro que quiere dar de baja al curso?[S/N]: ").lower()

                if op == "s":
                    ConsultasCurso.consBaja(nombre)
                    salir = True
                elif op == "n":
                    salir = True
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif fallos == 5:
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")


def consultar():
    nombre = None
    opcSalir = None
    fallos = 0
    while opcSalir != '0' and fallos < 5:
        try:
            aux = input("Introduzca el nombre del curso que quiera buscar o 0 pulsa para salir:")
            opcSalir = aux
            if opcSalir != 0:
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.noExistNombreCur(aux)
                nombre = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if fallos < 5 and opcSalir != 0:
            curso = ConsultasCurso.consBusqueda(nombre)
            for dato in curso:
                print(f'''---Curso---
Cod: {dato[0]}, ID_Profesor: {dato[1]}, Nombre: {dato[2]}, Descripcion: {dato[3]}, Alumnos: {dato[4]}''')
        elif fallos == 5:
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
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
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:")
            opcSalir = aux
            if (opcSalir != 0):
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
                    aux = input('Escriba el nuevo dni o pulse 0 para salir:')
                    opcSalir = aux
                    if (opcSalir != '0'):
                        VerificationExceptions.dniFormat(aux)
                        VerificationExceptions.existDni(aux)
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
    print(type(tabla))
    for tupla in tabla:
        print(f'''---Profesor---
Id: {tupla[0]}
DNI: {tupla[1]}
Nombre: {tupla[2]}
Direccion: {tupla[3]}
Telefono: {tupla[4]}
Cursos: {tupla[5]}''')