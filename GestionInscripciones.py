import ConsultasInscripciones
import VerificationExceptions
import ConsultasCurso
import ConsultasProfesor
import ConsultasAlumnos


def menu():
    """
    Funcion para el menu para la gestion de inscripciones
    :return:
    """
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
            if ConsultasCurso.hayCursos() and ConsultasAlumnos.hayAlumnos():
                matricularAlumno()
        elif opcion == "2":
            if ConsultasCurso.hayCursos() and ConsultasProfesor.hayProfesores():
                asignarProfesor()
        elif opcion == "3":
            if ConsultasInscripciones.hayAlumnosMatriculados():
                desmatricularAlumno()
        elif opcion == "4":
            if ConsultasInscripciones.hayProfesoresAsignados():
                desasignarProfesor()
        elif opcion == "0":
            print("Saliendo...")
            finMenuInscripciones = True
        else:
            print("Entrada no valida")


def matricularAlumno():
    """
    Funcion para matricular un alumno a un curso
    :return:
    """
    curso = None
    nombre = None
    apellido = None
    opcSalir = None
    fallos = 0
    salir = False
    while (opcSalir != '0' and fallos < 5 and not salir):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:").lower()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    curso = aux
            if (nombre is None and apellido is None and opcSalir != '0'):
                auxNom = input(
                    f"Introduzca el nombre del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:").lower()
                auxApe = input(
                    f"Introduzca el apellido del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:").lower()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(auxNom)
                    VerificationExceptions.hayAlgo(auxApe)
                    VerificationExceptions.noExisteAlumno(auxNom, auxApe)
                    nombre = auxNom
                    apellido = auxApe
                    salir = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    if (fallos < 5 and opcSalir != '0'):
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
    """
    Funcion para asignar un profesor a un curso
    :return:
    """
    curso = None
    dni = None
    opcSalir = None
    fallos = 0
    salir = False


    while (opcSalir != '0' and fallos < 5 and not salir):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al profesor o 0 pulsa para salir:").lower()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)

                    if ConsultasInscripciones.tiene_profe(aux):
                        seguir = None
                        while seguir != 's' and seguir != 'n':
                            seguir = input("El curso ya tiene asignado un profesor, quieres continuar? [S/N]").lower()

                            if seguir == 's':
                                curso = aux
                                if (dni is None and opcSalir != '0'):
                                    aux = input(
                                        f"Introduzca el dni del profesor que quiera asignar al curso {curso} o 0 pulsa para salir:").upper()
                                    opcSalir = aux
                                    if (opcSalir != '0'):
                                        VerificationExceptions.dniFormat(aux)
                                        VerificationExceptions.noExistDni(aux)
                                        dni = aux
                                        salir = True
                            elif seguir == 'n':
                                print("Volviendo...\n")

                            else:
                                print("Introduce una respuesta valida.")
                    else:
                        curso = aux
                        if (dni is None and opcSalir != '0'):
                            aux = input(
                                f"Introduzca el dni del profesor que quiera asignar al curso {curso} o 0 pulsa para salir:").upper()
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
    """
    Funcion que desmatricula un alumno de un curso
    :return:
    """
    curso = None
    nombre = None
    apellido = None
    idCurso = None
    idAlu = None
    opcSalir = None
    fallos = 0
    salir = False
    while (opcSalir != '0' and fallos < 5 and not salir):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera matricular al alumno o 0 pulsa para salir:").lower()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    idCurso = ConsultasInscripciones.obtIdCurso(aux)
                    curso = aux
            if (nombre is None and apellido is None and opcSalir != '0'):
                auxNom = input(
                    f"Introduzca el nombre del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:").lower()
                opcSalir = auxNom
                if (opcSalir != '0'):
                    auxApe = input(
                        f"Introduzca el apellido del alumno que quiera matricular al curso {curso} o 0 pulsa para salir:").lower()
                    opcSalir = auxApe
                    if (opcSalir != '0'):
                        VerificationExceptions.hayAlgo(auxNom)
                        VerificationExceptions.hayAlgo(auxApe)
                        VerificationExceptions.noExisteAlumno(auxNom, auxApe)
                        idAlu = ConsultasInscripciones.obtIdAlu(auxNom, auxApe)
                        VerificationExceptions.noExisteAlumnoEnAlumnoCurso(idAlu, idCurso)
                        nombre = aux
                        apellido = aux
                        salir = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    if (fallos < 5 and opcSalir != '0'):
        op = None
        salir = False
        while not salir and op is None:
            op = input(
                f"Seguro que quiere desmatricular al alumno {nombre, apellido} del curso {curso}?[S/N]").lower()
            if op == "s":
                ConsultasInscripciones.borrarAluCurso(idAlu, idCurso)
            elif op == "n":
                salir = True
                print("Saliendo sin guardar...")
            else:
                print("Entrada no valida.")
    elif (fallos == 5):
        print("Has superado el maximos de fallos permitidos que son 5")
    else:
        print("Saliendo...")


def desasignarProfesor():
    """
    Funcion que desasigna un profesor de un curso
    :return:
    """
    curso = None
    dni = None
    idCurso = None
    idProf = None
    opcSalir = None
    fallos = 0
    salir = False
    while (opcSalir != '0' and fallos < 5 and not salir):
        try:
            if (curso is None):
                aux = input("Introduzca el nombre del curso que quiera desasignar al profesor o 0 pulsa para salir:").lower()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    VerificationExceptions.noExistNombreCur(aux)
                    idCurso = ConsultasInscripciones.obtIdCurso(aux)
                    curso = aux
            if (dni is None and opcSalir != '0'):
                aux = input(
                    f"Introduzca el dni del profesor que quiera desasignar al curso {curso} o 0 pulsa para salir:").upper()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.dniFormat(aux)
                    VerificationExceptions.noExistDni(aux)
                    idProf = ConsultasInscripciones.obtIdProf(aux)
                    VerificationExceptions.noExisteProfesorEnCurso(idProf, idCurso)
                    dni = aux
                    salir = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
    if (fallos < 5 and opcSalir != '0'):
        op = None
        salir = False
        while not salir and op is None:
            op = input(
                f"Seguro que quiere matricular al profesor {dni} en el curso {curso}?[S/N]").lower()
            if op == "s":
                ConsultasInscripciones.borrarProfCurso(idProf, idCurso)
            elif op == "n":
                salir = True
                print("Saliendo sin guardar...")
            else:
                print("Entrada no valida.")
    elif (fallos == 5):
        print("Has superado el maximos de fallos permitidos que son 5")
    else:
        print("Saliendo...")
