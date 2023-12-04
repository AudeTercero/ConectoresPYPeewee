import VerificationExceptions
import ConsultasProfesor


def menu():
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
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            consultar()
        elif opcion == "5":
            mostrarTodos()
        elif opcion == "0":
            print("Saliendo...")
            finMenuProfesores = True
        else:
            print("Entrada no valida")


def alta():
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
                aux = input('Introduce el dni del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.dniFormat(aux)
                    dni = aux
                    intentos = 0
            if (nombre is None and opcSalir != '0'):
                aux = input('Introduce el nombre del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    nombre = aux
                    intentos = 0
            if (direccion is None and opcSalir != '0'):
                aux = input('Introduce la direccion del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    direccion = aux
                    intentos = 0
            if (telefono is None and opcSalir != '0'):
                aux = input('Introduce el telefeno del profesor o 0 para salir:\n')
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.validar_telefono(aux)
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
    dni = None
    opcSalir = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:")
            opcSalir = aux
            if (opcSalir != 0):
                VerificationExceptions.dniFormat(aux)
                dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if (fallos < 5 and opcSalir != 0):
            salir = False
            while not salir:
                op = input("Seguro que quiere dar de baja al profesor?[S/N]").lower()

                if op == "s":
                    ConsultasProfesor.consBaja(dni)
                    salir = True
                elif op == "n":
                    salir = True;
                    print("Saliendo sin guardar...")
                else:
                    print("Entrada no valida.")

        elif (fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")


def consultar():
    dni = None
    opcSalir = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        try:
            aux = input("Introduzca el dni del profesor que quiera buscar o 0 pulsa para salir:")
            opcSalir = aux
            if(opcSalir !=0):
                VerificationExceptions.dniFormat(aux)
                dni = aux
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            print(err)
        if(fallos <5 and opcSalir != 0):
            profesor = ConsultasProfesor.consBusqueda(dni)
            for tupla in profesor:
                print(f'''---Profesor---
Id: {tupla[0]}, DNI: {tupla[1]}, Nombre: {tupla[2]}, Direccion: {tupla[3]}, Telefono: {tupla[4]}''')
        elif(fallos == 5):
            print("Has superado el maximos de fallos permitidos que son 5")
        else:
            print("Saliendo...")





def modificar():
    print()


def mostrarTodos():
    tabla = ConsultasProfesor.mostrarTabla()
    print(type(tabla))
    for tupla in tabla:
        print(f'''---Profesor---
Id: {tupla[0]}
DNI: {tupla[1]}
Nombre: {tupla[2]}
Direccion: {tupla[3]}
Telefono: {tupla[4]}''')
