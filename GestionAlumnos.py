import VerificationExceptions
import ConsultasAlumnos


def menu():
    '''
    Metodo cuya funcion es simular un menu para interactuar con los alumnos de la base de datos
    :return:
    '''
    finMenuAlumnos = False
    while not finMenuAlumnos:
        opcion = input("\n\n\t[==== MENU ALUMNOS ====>\n"
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
            if ConsultasAlumnos.hayAlumnos():
                baja()
        elif opcion == "3":
            if ConsultasAlumnos.hayAlumnos():
                modificar()
        elif opcion == "4":
            if ConsultasAlumnos.hayAlumnos():
                consultar()
        elif opcion == "5":
            if ConsultasAlumnos.hayAlumnos():
                mostrarTodos()
        elif opcion == "0":
            print("Saliendo...")
            finMenuAlumnos = True
        else:
            print("Entrada no valida")


def alta():
    '''
    Metodo alta cuya funcion es aniadir alumnos a la base de datos
    :return:
    '''
    salir = False
    salir_sin_guardar = False
    cont = 0
    nombre = ""
    apellidos = ""
    direccion = ""
    telefono = ""
    fecha = ""

    while not salir and not salir_sin_guardar:
        if not cont == 5:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ").lower()
            if (nombre == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(nombre)
                    print("Nombre valido")
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
        if not cont == 5:
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ").lower()
            if (apellidos == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(apellidos)
                    print("Apellidos validos")
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
        if not cont == 5:
            telefono = input("Ingrese el telefono del alumno o pulse 0 para salir: ")
            if (telefono == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(telefono)
                    VerificationExceptions.validar_telefono(telefono)
                    print("Telefono valido")
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
        if not cont == 5:
            direccion = input("Ingrese la direccion del alumno o pulse 0 para salir: ")
            if (direccion == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(direccion)
                    print("Direccion valida")
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
        if not cont == 5:
            fecha = input("Ingrese la fecha del alumno o pulse 0 para salir: ")

            if fecha == "0":
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(fecha)
                    VerificationExceptions.formatoFecha(fecha)
                    print("Fecha valida")
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
        try:
            VerificationExceptions.existeAlumno(nombre, apellidos)
            ConsultasAlumnos.consAlta(nombre, apellidos, telefono, direccion, fecha)

        except VerificationExceptions.MisExceptions as err:
            print(err)


def baja():
    '''
    Metodo cuya funcion es borrar alumnos de la base de datos
    :return:
    '''
    salir = False
    salir_sin_guardar = False
    cont = 0
    nombre = None
    apellidos = None

    while not salir and not salir_sin_guardar:
        if not cont == 5:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ").lower()
            if (nombre == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(nombre)
                    print("Nombre valido")
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
        if not cont == 5:
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ").lower()
            if (apellidos == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(apellidos)
                    print("Apellidos validos")
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    salir = False
    if nombre is not None and apellidos is not None and not salir_sin_guardar:
        try:
            VerificationExceptions.noExisteAlumno(nombre, apellidos)

            while not salir:
                op = input("Seguro que quiere dar de baja al alumno?[S/N]").lower()

                if op == "s":
                    ConsultasAlumnos.consBaja(nombre, apellidos)
                    salir = True
                elif op == "n":
                    salir = True;
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        except VerificationExceptions.MisExceptions as err:
            print(err)
    else:
        print("Saliendo...")


def modificar():
    '''
    Metodo cuya funcion es modificar los distintos atributos de un usuario
    :return:
    '''
    salir = False
    salir_sin_guardar = False
    cont = 0
    nombre = None
    apellidos = None

    while not salir and not salir_sin_guardar:
        if not cont == 5:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ").lower()
            if (nombre == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(nombre)
                    print("Nombre valido")
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
        if not cont == 5:
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ").lower()
            if (apellidos == "0"):
                salir_sin_guardar = True
                salir = True
            else:
                try:
                    VerificationExceptions.hayAlgo(apellidos)
                    print("Apellidos validos")
                    salir = True

                except VerificationExceptions.MisExceptions as err:
                    cont += 1
                    print(err)
        else:
            print("\nHas llegado al limite de intentos.")
            salir_sin_guardar = True

    if nombre is not None and apellidos is not None and not salir_sin_guardar:
        try:
            VerificationExceptions.noExisteAlumno(nombre, apellidos)

            salir = False
            salir_sin_guardar = False

            while cont < 5 and not salir:
                op = input(''' 
                            ******* MODIFICACION ALUMNO *******
                            1.Nombre
                            2.Apellidos
                            3.Telefono
                            4.Direccion
                            5.Fecha
                            0.Salir
                            ''')

                if op == '1':
                    nuevoNombre = None
                    cont = 0
                    opSalir = None

                    while cont < 5 and nuevoNombre is None and opSalir != '0':
                        try:
                            aux = input('Escribe el nuevo nombre o pulsa 0 para salir:').lower()
                            opSalir = aux

                            if (opSalir != 0):
                                VerificationExceptions.hayAlgo(aux)
                                print("Nombre valido")
                                VerificationExceptions.existeAlumno(aux, apellidos)
                                nuevoNombre = aux

                        except VerificationExceptions.MisExceptions as err:
                            print(err)
                            cont += 1

                    if (cont < 5 and opSalir != '0'):
                        op = None
                        while not salir and op is None:
                            op = input("Seguro que quiere modificar el nombre del alumno?[S/N]").lower()
                            if op == "s":
                                ConsultasAlumnos.consModificar(nombre, apellidos, 'nombre', nuevoNombre)
                                print("Modificacion realizada correctamente")
                                nombre = nuevoNombre
                            elif op == "n":
                                salir = True
                                print("Saliendo sin guardar...")
                            else:
                                print("Entrada no valida.")
                    elif (cont == 5):
                        print("No puedes fallar mas de 5 veces")

                    else:
                        print("Saliendo...")

                elif op == '2':
                    nuevoApe = None
                    cont = 0
                    opSalir = None

                    while cont < 5 and nuevoApe is None and opSalir != '0':
                        try:
                            aux = input('Escribe los nuevos apellidos o pulsa 0 para salir:').lower()
                            opSalir = aux

                            if (opSalir != 0):
                                VerificationExceptions.hayAlgo(aux)
                                print("Apellidos validos")
                                VerificationExceptions.existeAlumno(nombre, nuevoApe)
                                nuevoApe = aux

                        except VerificationExceptions.MisExceptions as err:
                            print(err)
                            cont += 1

                    if (cont < 5 and opSalir != '0'):
                        op = None
                        while not salir and op is None:
                            op = input("Seguro que quiere modificar los apellidos del alumno?[S/N]").lower()
                            if op == "s":
                                ConsultasAlumnos.consModificar(nombre, apellidos, 'apellidos', nuevoApe)
                                print("Modificacion realizada correctamente")
                                apellidos = nuevoApe
                            elif op == "n":
                                salir = True
                                print("Saliendo sin guardar...")
                            else:
                                print("Entrada no valida.")
                    elif (cont == 5):
                        print("No puedes fallar mas de 5 veces")

                    else:
                        print("Saliendo...")

                elif op == '3':
                    nuevoTel = None
                    cont = 0
                    opSalir = None

                    while cont < 5 and nuevoTel is None and opSalir != '0':
                        try:
                            aux = input('Escribe el nuevo telefono o pulsa 0 para salir:')
                            opSalir = aux

                            if (opSalir != 0):
                                VerificationExceptions.validar_telefono(aux)
                                print("Telefono valido")
                                nuevoTel = aux

                        except VerificationExceptions.MisExceptions as err:
                            print(err)
                            cont += 1

                    if (cont < 5 and opSalir != '0'):
                        op = None
                        while not salir and op is None:
                            op = input("Seguro que quiere modificar el telefono del alumno?[S/N]").lower()
                            if op == "s":
                                ConsultasAlumnos.consModificar(nombre, apellidos, 'telefono', nuevoTel)
                                print("Modificacion realizada correctamente")
                            elif op == "n":
                                salir = True
                                print("Saliendo sin guardar...")
                            else:
                                print("Entrada no valida.")
                    elif (cont == 5):
                        print("No puedes fallar mas de 5 veces")

                    else:
                        print("Saliendo...")

                elif op == '4':
                    nuevaDir = None
                    cont = 0
                    opSalir = None

                    while cont < 5 and nuevaDir is None and opSalir != '0':
                        try:
                            aux = input('Escribe la nueva direccion o pulsa 0 para salir:')
                            opSalir = aux

                            if (opSalir != 0):
                                VerificationExceptions.hayAlgo(aux)
                                print("Direccion valida")
                                nuevaDir = aux

                        except VerificationExceptions.MisExceptions as err:
                            print(err)
                            cont += 1

                    if (cont < 5 and opSalir != '0'):
                        op = None
                        while not salir and op is None:
                            op = input("Seguro que quiere modificar la direccion del alumno?[S/N]").lower()
                            if op == "s":
                                ConsultasAlumnos.consModificar(nombre, apellidos, 'direccion', nuevaDir)
                                print("Modificacion realizada correctamente")
                            elif op == "n":
                                salir = True
                                print("Saliendo sin guardar...")
                            else:
                                print("Entrada no valida.")
                    elif (cont == 5):
                        print("No puedes fallar mas de 5 veces")

                    else:
                        print("Saliendo...")

                elif op == '4':
                    nuevaFech = None
                    cont = 0
                    opSalir = None

                    while cont < 5 and nuevaFech is None and opSalir != '0':
                        try:
                            aux = input('Escribe la nueva fecha de nacimiento o pulsa 0 para salir:')
                            opSalir = aux

                            if (opSalir != 0):
                                VerificationExceptions.formatoFecha(aux)
                                print("Fecha valida")
                                nuevaFech = aux

                        except VerificationExceptions.MisExceptions as err:
                            print(err)
                            cont += 1

                    if (cont < 5 and opSalir != '0'):
                        op = None
                        while not salir and op is None:
                            op = input("Seguro que quiere modificar la fecha de nacimiento del alumno?[S/N]").lower()
                            if op == "s":
                                ConsultasAlumnos.consModificar(nombre, apellidos, 'fecha_nac', nuevaFech)
                                print("Modificacion realizada correctamente")
                            elif op == "n":
                                salir = True
                                print("Saliendo sin guardar...")
                            else:
                                print("Entrada no valida.")
                    elif (cont == 5):
                        print("No puedes fallar mas de 5 veces")

                    else:
                        print("Saliendo...")

                elif op == '0':
                    salir = True

        except VerificationExceptions.MisExceptions as err:
            print(err)
    else:
        print("Saliendo...")


def consultar():
    '''
    Metodo cuya funcion es mostrar los atributos de un alumno en especifico
    :return:
    '''
    salir = False
    salir_sin_guardar = False
    cont = 0
    nombre = None
    apellidos = None

    while not salir and not salir_sin_guardar:
        if not cont == 5:
            nombre = input("Ingrese el nombre del alumno o pulse 0 para salir: ").lower()
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
            apellidos = input("Ingrese los apellidos del alumno o pulse 0 para salir: ").lower()
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

    if nombre is not None and apellidos is not None and not salir_sin_guardar:
        try:
            VerificationExceptions.noExisteAlumno(nombre, apellidos)
            resultados = ConsultasAlumnos.consBuscar(nombre, apellidos)

            if resultados is not None:
                for r in resultados:
                    print(f'''---Alumno---
        ID: {r[0]}
        Nombre: {r[1]}
        Apellidos: {r[2]}
        Telefono: {r[3]}
        Direccion: {r[4]}
        Fecha de Nacimiento: {r[5]}
        Cursos: {r[6]}''')

        except VerificationExceptions.MisExceptions as err:
            print(err)


def mostrarTodos():
    '''
    Metodo cuya funcion es mostrar todos los alumnos y sus atributos dentro de la base de datos
    :return:
    '''
    tabla = ConsultasAlumnos.consMostrarAlumnos()
    for tupla in tabla:
        print(f'''---Alumno---
        ID: {tupla[0]}
        Nombre: {tupla[1]}
        Apellidos: {tupla[2]}
        Telefono: {tupla[3]}
        Direccion: {tupla[4]}
        Fecha de Nacimiento: {tupla[5]}
        Cursos: {tupla[6]}''')

