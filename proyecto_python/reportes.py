import json
from datetime import datetime

def herramientas_stock_bajo():

    with open("herramientas.json", "r") as f:
        herramientas = json.load(f)

    print("\n--- HERRAMIENTAS CON STOCK BAJO ---")

    for h in herramientas:
        if h["cantidad_disponible"] < 3:
            print(f'ID: {h["id"]} | Nombre: {h["nombre"]} | Disponible: {h["cantidad_disponible"]}')

def prestamos_activos_vencidos():

    with open("prestamos.json", "r") as f:
        prestamos = json.load(f)

    hoy = datetime.today().date()

    print("\n--- PRÉSTAMOS ACTIVOS Y VENCIDOS ---")

    for p in prestamos:
        if p["estado"] == "aprobado":

            fecha_dev = datetime.strptime(p["fecha_devolucion"], "%Y-%m-%d").date()

            if fecha_dev >= hoy:
                estado = "Activo"
            else:
                estado = "Vencido"

            print(f'ID: {p["id"]} | Usuario: {p["usuario_id"]} | Estado: {estado}')

def historial_usuario():

    with open("prestamos.json", "r") as f:
        prestamos = json.load(f)

    usuario_id = int(input("Ingrese ID del usuario: "))

    print("\n--- HISTORIAL DEL USUARIO ---")

    for p in prestamos:
        if p["usuario_id"] == usuario_id:
            print(f'Préstamo ID: {p["id"]} | Estado: {p["estado"]} | Cantidad: {p["cantidad"]}')

def herramientas_mas_solicitadas():

    with open("prestamos.json", "r") as f:
        prestamos = json.load(f)

    contador = {}

    for p in prestamos:
        herramienta_id = p["herramienta_id"]
        contador[herramienta_id] = contador.get(herramienta_id, 0) + p["cantidad"]

    print("\n--- HERRAMIENTAS MÁS SOLICITADAS ---")

    for h_id, total in sorted(contador.items(), key=lambda x: x[1], reverse=True):
        print(f'Herramienta ID: {h_id} | Total solicitadas: {total}')

def usuarios_mas_activos():

    with open("prestamos.json", "r") as f:
        prestamos = json.load(f)

    contador = {}

    for p in prestamos:
        usuario_id = p["usuario_id"]
        contador[usuario_id] = contador.get(usuario_id, 0) + p["cantidad"]

    print("\n--- USUARIOS MÁS ACTIVOS ---")

    for u_id, total in sorted(contador.items(), key=lambda x: x[1], reverse=True):
        print(f'Usuario ID: {u_id} | Total herramientas solicitadas: {total}')
    