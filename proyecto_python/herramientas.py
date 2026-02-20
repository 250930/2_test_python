import json
from datos import registro_eventos

def ver_herramientas_disponibles(datos):
    if not datos:
        print("No hay herramientas disponibles.")
        return

    print("\n" + "="*90)
    print(f"{'ID':<5} {'NOMBRE':<50} {'CATEGORIA':<15} {'DISP.':<8} {'ESTADO':<20} {'VALOR':<10}")
    print("="*90)

    for herramienta in datos:
        print(f"{herramienta['id']:<5} "
              f"{herramienta['nombre']:<50} "
              f"{herramienta['categoria']:<15} "
              f"{herramienta['cantidad_disponible']:<8} "
              f"{herramienta['estado']:<20} "
              f"{herramienta['valor_estimado']:<10}")

    print("="*90)


def agregar_herramienta():
    try:
        with open("herramientas.json", "r") as arch:
            datos = json.load(arch)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = []

    id_herramienta = max([h["id"] for h in datos], default=0) + 1

    nombre = input("Ingrese el nombre: ")
    categoria = input("Ingrese la categoría: ")
    cantidad_disponible = int(input("Ingrese la cantidad disponible: "))
    estado = input("Ingrese el estado: ")
    valor_estimado = float(input("Ingrese el valor estimado: "))

    nueva_herramienta = {
        "id": id_herramienta,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad_disponible": cantidad_disponible,
        "estado": estado,
        "valor_estimado": valor_estimado
    }

    datos.append(nueva_herramienta)

    with open("herramientas.json", "w") as arch:
        json.dump(datos, arch, indent=4)

    registro_eventos(f"Herramienta ID {id_herramienta} agregada.")
    print("Herramienta agregada correctamente.")


def modificar_herramienta():
    with open("herramientas.json", "r") as arch:
        datos = json.load(arch)

    id_herramienta = int(input("Ingrese el ID de la herramienta a modificar: "))

    for herramienta in datos:
        if herramienta["id"] == id_herramienta:

            nombre = input(f"Nombre ({herramienta['nombre']}): ") or herramienta['nombre']
            categoria = input(f"Categoria ({herramienta['categoria']}): ") or herramienta['categoria']
            cantidad_disponible = input(f"Cantidad disponible ({herramienta['cantidad_disponible']}): ") or herramienta['cantidad_disponible']
            estado = input(f"Estado ({herramienta['estado']}): ") or herramienta['estado']
            valor_estimado = input(f"Valor estimado ({herramienta['valor_estimado']}): ") or herramienta['valor_estimado']

            herramienta.update({
                "nombre": nombre,
                "categoria": categoria,
                "cantidad_disponible": int(cantidad_disponible),
                "estado": estado,
                "valor_estimado": float(valor_estimado)
            })

            with open("herramientas.json", "w") as arch:
                json.dump(datos, arch, indent=4)

            registro_eventos(f"Herramienta ID {id_herramienta} modificada.")
            print("Herramienta modificada exitosamente.")
            return

    print("Herramienta no encontrada.")
    registro_eventos(f"Intento fallido de modificar herramienta ID {id_herramienta}.")


def eliminar_herramienta(id_herramienta):
    try:
        with open("herramientas.json", "r") as arch:
            datos = json.load(arch)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error al leer el archivo.")
        return

    herramienta_encontrada = None

    for herramienta in datos:
        if herramienta["id"] == id_herramienta:
            herramienta_encontrada = herramienta
            break

    if herramienta_encontrada is None:
        print("ID no existe.")
        registro_eventos(f"Intento fallido de eliminar herramienta ID {id_herramienta}.")
        return

    datos.remove(herramienta_encontrada)

    with open("herramientas.json", "w") as arch:
        json.dump(datos, arch, indent=4)

    registro_eventos(f"Herramienta ID {id_herramienta} eliminada.")
    print("Herramienta eliminada correctamente.")


def solcitar_herramienta():
    try:
        with open("prestamos.json", "r") as arch:
            prestamos = json.load(arch)
    except (FileNotFoundError, json.JSONDecodeError):
        prestamos = []

    with open("herramientas.json", "r") as arch:
        herramientas = json.load(arch)

    nuevo_id = max([p["id"] for p in prestamos], default=0) + 1

    usuario_id = int(input("Ingrese el ID del usuario: "))
    herramienta_id = int(input("Ingrese el ID de la herramienta: "))
    cantidad = int(input("Ingrese la cantidad a prestar: "))
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_devolucion = input("Ingrese la fecha estimada de devolución (YYYY-MM-DD): ")
    observaciones = input("Ingrese observaciones: ")

    herramienta_encontrada = None

    for herramienta in herramientas:
        if herramienta["id"] == herramienta_id:
            herramienta_encontrada = herramienta
            break

    if herramienta_encontrada is None:
        print("Herramienta no encontrada.")
        registro_eventos(f"Intento de préstamo con herramienta inexistente ID {herramienta_id}.")
        return

    nuevo_prestamo = {
        "id": nuevo_id,
        "usuario_id": usuario_id,
        "herramienta_id": herramienta_id,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_devolucion": fecha_devolucion,
        "estado": "en espera",
        "observaciones": observaciones
    }

    prestamos.append(nuevo_prestamo)

    with open("prestamos.json", "w") as arch:
        json.dump(prestamos, arch, indent=4)

    registro_eventos(f"Préstamo ID {nuevo_id} registrado en espera.")
    print(f"Préstamo registrado correctamente con ID {nuevo_id}.")


def devolver_herramienta():
    try:
        with open("prestamos.json", "r") as arch:
            prestamos = json.load(arch)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay préstamos registrados.")
        return

    try:
        with open("herramientas.json", "r") as arch:
            herramientas = json.load(arch)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al leer herramientas.")
        return

    id_prestamo = int(input("Ingrese el ID del préstamo: "))

    for prestamo in prestamos:
        if prestamo["id"] == id_prestamo:

            if prestamo["estado"] != "aprobado":
                print("El préstamo no está aprobado o ya fue devuelto.")
                registro_eventos(f"Intento inválido de devolución préstamo ID {id_prestamo}.")
                return

            for herramienta in herramientas:
                if herramienta["id"] == prestamo["herramienta_id"]:

                    herramienta["cantidad_disponible"] += prestamo["cantidad"]
                    prestamo["estado"] = "devuelto"

                    with open("herramientas.json", "w") as arch:
                        json.dump(herramientas, arch, indent=4)

                    with open("prestamos.json", "w") as arch:
                        json.dump(prestamos, arch, indent=4)

                    registro_eventos(f"Préstamo ID {id_prestamo} devuelto.")
                    print("Herramienta devuelta correctamente.")
                    return

    print("Préstamo no encontrado.")
    registro_eventos(f"Intento de devolución préstamo inexistente ID {id_prestamo}.")
