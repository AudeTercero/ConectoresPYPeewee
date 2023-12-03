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
            print("Matricular Alumno")
        elif opcion == "2":
            print("Asignar Profesor")
        elif opcion == "3":
            print("Desmatricular Alumno")
        elif opcion == "4":
            print("Desasignar Profesor")
        elif opcion == "0":
            print("Saliendo...")
            finMenuInscripciones = True
        else:
            print("Entrada no valida")
