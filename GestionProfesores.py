
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
            finMenuProfesores = True
        else:
            print("Entrada no valida")

def alta():
