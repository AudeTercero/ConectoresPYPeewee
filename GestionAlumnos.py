import VerificationExceptions


def menu():
    finMenuAlumnos = False
    while not finMenuAlumnos:
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
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            consultar()
        elif opcion == "5":
            mostrarTodos()
        elif opcion == "0":
            print("Saliendo...")
            finMenuAlumnos = True
        else:
            print("Entrada no valida")


def alta():
    salir = False
    salir_sin_guardar = False
    cont = 0

    while not salir and not salir_sin_guardar:
        if not cont == 3:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ")
            if (nombre == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(nombre)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ")
            if (apellidos == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(apellidos)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            telefono = input("Ingrese el telefono del alumno o pulse 0 para salir: ")
            if (telefono == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(telefono)
                    VerificationExceptions.validar_telefono(telefono)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            direccion = input("Ingrese la direccion del alumno o pulse 0 para salir: ")
            if (direccion == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(direccion)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            fecha = input("Ingrese la fecha del alumno o pulse 0 para salir: ")
            if (fecha == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(fecha)
                    VerificationExceptions.formatoFecha(fecha)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    if salir_sin_guardar:
        print("Saliendo...")
    else:
        print()
        # Mandar los datos recogidos


def baja():
    print()


def modificar():
    print()


def consultar():
    salir = False
    salir_sin_guardar = False
    cont = 0
    nombre = None
    apellidos = None

    while not salir and not salir_sin_guardar:
        if not cont == 3:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ")
            if (nombre == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(nombre)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    cont = 0
    while not salir and not salir_sin_guardar:
        if not cont == 3:
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ")
            if (apellidos == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(apellidos)
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    if nombre is not None and apellidos is not None:
        cursor.execute("SELECT * FROM alumnos WHERE nombre = '" + nombre + "' AND apellidos = '" + apellidos + "'")
        alumno = cursor.fetchone()

    if alumno:
        print("---Alumno---")
        print(f"ID:{alumno[0]}")
        print(f"Nombre:{alumno[1]}")
        print(f"Apellidos:{alumno[2]}")
        print(f"Telefono:{alumno[3]}")
        print(f"Direccion:{alumno[4]}")
        print(f"Fecha de Nacimiento:{alumno[5]}")
    else:
        print(f"No se encontro un alumno con ese nombre y esos apellidos")

def mostrarTodos():
    print()
