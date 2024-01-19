from ConexionBBDD import conect
from GestionAlumnos import menu as menuAlumnos
from GestionProfesores import menu as menuProfesores
from GestionCursos import menu as menuCursos
from GestionInscripciones import menu as menuInscripciones
from Tablas_BBDD import crear_tabla


con = conect()
if(con is not None):
    crear_tabla()
    print("Inicio Practica Conectores")
    finMenuPrincipal = False
    while not finMenuPrincipal:
        opcion = input("\n\n[==== MENU PRINCIPAL ====>\n"
                       "[1. Gestion Alumnos\n"
                       "[2. Gestion Profesores\n"
                       "[3. Gestion Cursos\n"
                       "[4. Inscripciones\n"
                       "[0. Salir\n"
                       "[===== Opcion: ")
        if opcion == "1":
            menuAlumnos()
        elif opcion == "2":
            menuProfesores()
        elif opcion == "3":
            menuCursos()
        elif opcion == "4":
            menuInscripciones()
        elif opcion == "0":
            print("Saliendo...")
            finMenuPrincipal = True
        else:
            print("Entrada no valida")
    print("Fin Practica Conectores")
    con.close()
else:
    print("Debes conectar la base de datos primero")
