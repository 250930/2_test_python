import json
from datetime import datetime
    
def prestamos_pendientes():

    with open("prestamos.json", "r") as arch:
        prestamos = json.load(arch)

    with open("herramientas.json", "r") as arch:
        herramientas = json.load(arch)

    id_prestamo = int(input("Ingrese el ID del préstamo: "))

    for prestamo in prestamos:

        if prestamo["id"] == id_prestamo:

            print("\n--- DATOS DEL PRÉSTAMO ---")
            print("ID:", prestamo["id"])
            print("Herramienta ID:", prestamo["herramienta_id"])
            print("Cantidad:", prestamo["cantidad"])
            print("Estado:", prestamo["estado"])

            if prestamo["estado"] != "en espera":
                print("Este préstamo ya fue procesado.")
                registro_eventos(f"Intento de reprocesar préstamo ID {prestamo['id']}.")
                return

            print("\n1. Aprobar")
            print("2. Rechazar")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":  

                for herramienta in herramientas:

                    if herramienta["id"] == prestamo["herramienta_id"]:

                        if herramienta["cantidad_disponible"] >= prestamo["cantidad"]:

                            herramienta["cantidad_disponible"] -= prestamo["cantidad"]
                            prestamo["estado"] = "aprobado"

                            print("Préstamo aprobado correctamente ")
                            registro_eventos(f"Préstamo ID {prestamo['id']} aprobado correctamente.")

                        else:
                            print("Stock insuficiente ")
                            registro_eventos(f"Error: Stock insuficiente para préstamo ID {prestamo['id']}.")
                            return
                        break

            elif opcion == "2": 

                prestamo["estado"] = "rechazado"
                print("Préstamo rechazado ")
                registro_eventos(f"Prestamo ID {prestamo['id']} rechazado.")

            else:
                print("Opción inválida")
                registro_eventos(f"Opcion inválida al procesar préstamo ID {prestamo['id']}.")
                return

            break

    else:
        print("Préstamo no encontrado")
        registro_eventos(f"Intento de acceder a préstamo inexistente ID {id_prestamo}.")
        return

    with open("prestamos.json", "w") as arch:
        json.dump(prestamos, arch, indent=4)

    with open("herramientas.json", "w") as arch:
        json.dump(herramientas, arch, indent=4)
def consultas_reportes():
    while True:
        print("""\n--- REPORTES ---
        1. Herramientas con stock bajo
        2. Préstamos activos y vencidos
        3. Historial de usuario
        4. Herramientas más solicitadas
        5. Usuarios más activos
        6. Volver""")

        opcion = input("Seleccione: ")

        from reportes import  herramientas_stock_bajo, prestamos_activos_vencidos, historial_usuario,  herramientas_mas_solicitadas,  usuarios_mas_activos

        if opcion == "1":
            herramientas_stock_bajo()
        elif opcion == "2":
            prestamos_activos_vencidos()
        elif opcion == "3":
            historial_usuario()
        elif opcion == "4":
            herramientas_mas_solicitadas()
        elif opcion == "5":
            usuarios_mas_activos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")
def registro_eventos(mensaje):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("eventos.txt", "a") as archivo:
        archivo.write(f"[{fecha_hora}] {mensaje}\n")
def mostrar_logs():
    try:
        with open("eventos.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\n===== REGISTRO DE EVENTOS =====")
                print(contenido)
            else:
                print("No hay eventos registrados.")
    except FileNotFoundError:
        print("Aún no se ha creado el archivo de eventos.")
