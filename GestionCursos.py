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
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            consultar()
        elif opcion == "5":
            mostrarTodos()
        elif opcion == "0":
            print("Saliendo...")
            finMenuCursos = True
        else:
            print("Entrada no valida")


def alta():
    """
    Funcion de alta que agrega un curso
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
                aux = input('Introduce el nombre del curso o 0 para salir:\n').lower()
                opcSalir = aux
                if opcSalir != '0':
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.existNombreCur(aux)
                    nombre = aux
                    intentos = 0
                    print("Nombre correcto")
            if descripcion is None and opcSalir != '0':
                aux = input('Introduce la descripcion del curso o 0 para salir:\n')
                opcSalir = aux
                if opcSalir != '0':
                    VerificationExceptions.hayAlgo(aux)
                    descripcion = aux
                    intentos = 0
                    salir = True
                    print("Descripcion Correcta")
            if opcSalir == '0':
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            print(err)

    if intentos < 5 and opcSalir != '0':
        ConsultasCurso.consAlta(nombre, descripcion)
        print("Alta realizada")
    elif opcSalir == '0':
        print("Saliendo")
    else:
        print("Se han superado el maximo de errores.")


def baja():
    """
    Funcion que da de baja un curso
    :return:
    """
    nombre = None
    opcSalir = None
    fallos = 0
    finBaja = False
    while not finBaja and opcSalir != '0' and fallos < 5:
        try:
            aux = input("Introduzca el nombre del curso que quiera buscar o 0 pulsa para salir: ").lower()
            opcSalir = aux
            if opcSalir != '0':
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.noExistNombreCur(aux)
                nombre = aux
                finBaja = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)

    if fallos < 5 and opcSalir != '0':
        salir = False
        while not salir:
            op = input("Seguro que quiere dar de baja al curso?[S/N]: ").lower()

            if op == "s":
                ConsultasCurso.consBaja(nombre)
                print("Baja realizada con exito")
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
    """
    Funcion que permite mostrar el contenido de un curso
    :return:
    """
    nombre = None
    opcSalir = None
    fallos = 0
    finConsulta = False
    while not finConsulta and opcSalir != '0' and fallos < 5:
        try:
            aux = input("Introduzca el nombre del curso que quiera buscar o 0 pulsa para salir:").lower()
            opcSalir = aux
            if opcSalir != '0':
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.noExistNombreCur(aux)
                nombre = aux
                finConsulta = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    if fallos < 5 and opcSalir != '0':
        curso = ConsultasCurso.consBusqueda(nombre)
        for dato in curso:
            print(dato)
    elif fallos == 5:
        print("Has superado el maximos de fallos permitidos que son 5")
    else:
        print("Saliendo...")


def modificar():
    """
    Funcion que permite modificar los campos de un curso
    :return:
    """
    nombre = None
    opcSalir = None
    fallos = 0
    salir = False
    while not salir and opcSalir != '0' and fallos < 5:
        try:
            aux = input("Introduzca el nombre del curso que quiera buscar o 0 pulsa para salir:").lower()
            opcSalir = aux
            if opcSalir != '0':
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.noExistNombreCur(aux)
                nombre = aux
                salir = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    salir = False
    while fallos < 5 and not salir and opcSalir != '0':
        opc = input(''' 
                    ******* MODIFICACION CURSO *******
                    1.Nombre
                    2.Descripcion
                    0.Salir
                    ''')
        if opc == '1':
            nuevoNombre = None
            fallos = 0
            opcSalir = None
            salirNombre = False
            while not salirNombre and fallos < 5 and opcSalir != '0':
                try:
                    aux = input('Escriba el nuevo nombre o pulse 0 para salir:').lower()
                    opcSalir = aux
                    if opcSalir != '0':
                        VerificationExceptions.hayAlgo(aux)
                        VerificationExceptions.existNombreCur(aux)
                        nuevoNombre = aux
                        salirNombre = True
                        print("Nombre correcto")
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if fallos < 5 and opcSalir != '0':
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar el nombre del curso?[S/N]: ").lower()
                    if op == "s":
                        ConsultasCurso.consModificar(nombre, 'nombre', nuevoNombre)
                        print("Modificacion realizada correctamente")
                        nombre = nuevoNombre
                    elif op == "n":
                        salir = True
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif fallos == 5:
                print("No puedes fallar mas de 5 veces")

            else:
                print("Saliendo...")

        elif opc == '2':
            nuevaDescripcion = None
            fallos = 0
            opcSalir = None
            while fallos < 5 and nuevaDescripcion is None and opcSalir != '0':
                try:
                    aux = input('Escriba la nueva descripcion o pulse 0 para salir:')
                    opcSalir = aux
                    if opcSalir != '0':
                        VerificationExceptions.hayAlgo(aux)
                        nuevaDescripcion = aux
                        print("Descripcion Correcta")
                except VerificationExceptions.MisExceptions as err:
                    print(err)
                    fallos += 1
            if fallos < 5 and opcSalir != '0':
                op = None
                while not salir and op is None:
                    op = input("Seguro que quiere modificar la descripcion del curso?[S/N]: ").lower()
                    if op == "s":
                        ConsultasCurso.consModificar(nombre, 'descripcion', nuevaDescripcion)
                        print("Modificacion realizada correctamente")
                    elif op == "n":
                        salir = True
                        print("Saliendo sin guardar...")
                    else:
                        print("Entrada no valida.")
            elif fallos == 5:
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
    Funcion que muestra todos los curso
    :return:
    """
    tabla = ConsultasCurso.mostrarTabla()
    print("--- CURSOS ---")
    for tupla in tabla:
        print(f"Cod: {tupla[0]}  Nombre: {tupla[2]}  Descripcion: {tupla[3]}  Profesor: {tupla[1]}")
    print("--------------")
