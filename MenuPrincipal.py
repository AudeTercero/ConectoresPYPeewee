print("Inicio Practica Conectores")

finMenuPrincipal = False
while not finMenuPrincipal:
    opcion = input("\n\n[==== MENU PRINCIPAL ====>\n"
                   "[1. Gestion Alumnos\n"
                   "[2. Gestion Profesores\n"
                   "[3. Gestion Cursos\n"
                   "[4. Inscripciones\n"
                   "[0. Gestion Alumnos\n"
                   "[===== Opcion: ")
    if opcion == "1":
        print("Gestion Alumnos")
    elif opcion == "2":
        print("Gestion Profesores")
    elif opcion == "3":
        print("Gestion Cursos")
    elif opcion == "4":
        print("Inscripciones")
    elif opcion == "0":
        print("Saliendo...")
        finMenuPrincipal = True
    else:
        print("Entrada no valida")
print("Fin Practica Conectores")
