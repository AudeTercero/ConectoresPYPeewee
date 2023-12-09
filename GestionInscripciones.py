import ConsultasInscripciones
import VerificationExceptions


def menu():
    finMenuInscripciones = False
    while not finMenuInscripciones:
        opcion = input("\n\n\t[==== MENU INSCRIPCIONES ====>\n"
                       "\t[1. Matricular Alumno\n"
                       "\t[2. Asignar Profesor\n"
                       "\t[3. Desmatricular Alumno\n"
                       "\t[4. Desasignar Profesor\n"
                       "\t[0. Salir\n"
                       "\t[===== Opcion: ")
        if opcion == "1":
            matricularAlumno()
        elif opcion == "2":
            asignarProfesor()
        elif opcion == "3":
            desmatricularAlumno()
        elif opcion == "4":
            desasignarProfesro()
        elif opcion == "0":
            print("Saliendo...")
            finMenuInscripciones = True
        else:
            print("Entrada no valida")


def matricularAlumno():
    curso = None
    nombre = None
    apellido = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    curso = aux
            if (nombre is None and apellido is None):
                auxNom = input(
                    f"Introduzca el nombre del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:")
                auxApe = input(
                    f"Introduzca el apellido del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)

                    '''Aqui comprobacion de nombre y apellido'''

                    nombre = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if (fallos < 5 and opcSalir != 0):
            op = None
            salir = False
            while not salir and op is None:
                op = input(
                    f"Seguro que quiere matricular al alumno {nombre, apellido} en el curso {curso}?[S/N]").lower()
                if op == "s":
                    ConsultasInscripciones.matAlu(curso, nombre, apellido)
                    print(f"El alumno {nombre, apellido} ha sido matriculado correctamente en el curso {curso}")
                elif op == "n":
                    salir = True
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")


def asignarProfesor():
    curso = None
    dni = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    curso = aux
            if (dni is None):
                aux = input(
                    f"Introduzca el dni del profesor que quiera asignar al curso {curso} o 0 pulsa para salir:")

                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.dniFormat(aux)
                    VerificationExceptions.noExistDni(aux)
                    dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if (fallos < 5 and opcSalir != 0):
            op = None
            salir = False
            while not salir and op is None:
                op = input(
                    f"Seguro que quiere matricular al profesor {dni} en el curso {curso}?[S/N]").lower()
                if op == "s":
                    ConsultasInscripciones.asigProf(curso, dni)
                    print(f"El profesro con el dni {dni} ha sido asignado correctamente en el curso {curso}")
                elif op == "n":
                    salir = True
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")


def desmatricularAlumno():
    curso = None
    nombre = None
    apellido = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    curso = aux
            if (nombre is None and apellido is None):
                auxNom = input(
                    f"Introduzca el nombre del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:")
                auxApe = input(
                    f"Introduzca el apellido del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)

                    '''Aqui comprobacion de nombre y apellido'''

                    nombre = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if (fallos < 5 and opcSalir != 0):
            op = None
            salir = False
            while not salir and op is None:
                op = input(
                    f"Seguro que quiere matricular al alumno {nombre, apellido} en el curso {curso}?[S/N]").lower()
                if op == "s":
                    ConsultasInscripciones.matAlu(curso, nombre, apellido)
                    print(f"El alumno {nombre, apellido} ha sido matriculado correctamente en el curso {curso}")
                elif op == "n":
                    salir = True
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")


def desasignarProfesro():
    curso = None
    dni = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:")
                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    curso = aux
            if (dni is None):
                aux = input(
                    f"Introduzca el dni del profesor que quiera asignar al curso {curso} o 0 pulsa para salir:")

                opcSalir = aux
                if (opcSalir != 0):
                    VerificationExceptions.dniFormat(aux)
                    VerificationExceptions.noExistDni(aux)
                    dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if (fallos < 5 and opcSalir != 0):
            op = None
            salir = False
            while not salir and op is None:
                op = input(
                    f"Seguro que quiere matricular al profesor {dni} en el curso {curso}?[S/N]").lower()
                if op == "s":
                    ConsultasInscripciones.asigProf(curso, dni)
                    print(f"El profesro con el dni {dni} ha sido asignado correctamente en el curso {curso}")
                elif op == "n":
                    salir = True
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")
