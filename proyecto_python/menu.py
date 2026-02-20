
import json

with open("usuarios.json", "r") as arch:
    usuarios = json.load(arch)

with open("herramientas.json", "r") as arch:
    herramientas = json.load(arch)

def menu_usuarios():

    while True:
        print("""
    ================================
        BIENVENIDO AL MENU DE USUARIO
    ================================
    1. Ver herramientas disponibles
    2. Solocitar prestamo de herramienta
    3. Devolver herramienta
    4. Salir
    ================================
        
        """)
        from herramientas import ver_herramientas_disponibles, solcitar_herramienta, devolver_herramienta
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            ver_herramientas_disponibles(herramientas)       
        elif opcion == "2":
            solcitar_herramienta()  
        elif opcion == "3":
            devolver_herramienta()
        elif opcion == "4":
            print("Saliendo del menu de usuario...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")





def menu_admin():

    while True:
        print("""
    ===============================
        BIENVENIDO MENU ADMINISTRADOR
    ===============================
    1. Ver herramientas disponibles
    2. Agregar herramienta
    3. Modificar herramienta
    4. Eliminar herramienta
    5. Agregar usuario
    6. Actualizar usuario
    7. Prestamos pendientes
    8. Eliminar usuario
    9.Consultas y reportes
    10.Registro de eventos (logs)
    11. Salir
    ================================
        """)
        op = str(input("Ingrese una opcion: "))
        from herramientas import ver_herramientas_disponibles,agregar_herramienta,  eliminar_herramienta, modificar_herramienta
        from usurios import agregar_usuario, eliminar_usuario, actualizar_usuario
        from datos import prestamos_pendientes, consultas_reportes, registro_eventos, mostrar_logs
        if op == "1":
            ver_herramientas_disponibles(herramientas)
        elif op == "2":
            agregar_herramienta()
        elif op == "3":
            modificar_herramienta()
        elif op == "4":
            id_herramienta = int(input("Ingrese el ID de la herramienta para eliminar:"))            
            eliminar_herramienta(id_herramienta)
        elif op == "5":
            agregar_usuario()
        elif op == "6":
            actualizar_usuario()
        elif op == "7":
            prestamos_pendientes()
        elif op == "8":
            id_usuario = int(input("Ingrese el ID del usuario para eliminar:"))  
            eliminar_usuario(id_usuario)
        elif op == "9":
            consultas_reportes()
        elif op == "10":
            mostrar_logs()
        elif op == "11":
            print("Saliendo del menu de administrador...")

            break

        else:
            print("Opcion no valida. Intente de nuevo.")

def inicio():
    while True:
        print("""
        =========================
        PRESTAMO DE HERRAMIENTAS
        =========================
        1. Usuario
        2. Administrador
        3. Salir
        =========================
        """)
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            nom = input("Ingrese su nombre: ")
            id = input("Ingrese su ID: ")
            

            for datos in usuarios:
                if nom.lower() == datos["nombres"].lower() and id == str(datos["id"]) and datos["tipo_usuario"] == "residente":
                    menu_usuarios()
                    break
            else:
                print("Usuario no encontrado.")

        elif opcion == "2":
            nom = input("Ingrese su nombre: ")
            id = input("Ingrese su ID: ")
            
            for datos in usuarios:
            
                if nom.lower() == datos["nombres"].lower() and id == str(datos["id"]) and datos["tipo_usuario"] == "administrador":
                    menu_admin()
                    break
            else:
                print("Usuario no encontrado.")
            
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
inicio()

