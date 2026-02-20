# ==========================================================
# SISTEMA COMPLETO DE PRÉSTAMOS DE HERRAMIENTAS - TALLER
# Incluye 30+ funciones para evaluación
# ==========================================================

import json
from datetime import datetime

# ==========================================================
# FUNCIONES BASE (PERSISTENCIA DE DATOS)
# ==========================================================

def cargar_datos(ruta):
    """Carga datos desde un archivo JSON."""
    try:
        with open(ruta, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(ruta, datos):
    """Guarda datos en archivo JSON."""
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# ==========================================================
# VALIDACIONES
# ==========================================================

def validar_texto_no_vacio(texto):
    return texto.strip() != ""

def validar_stock(stock):
    return isinstance(stock, int) and stock >= 0

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# ==========================================================
# GENERADOR DE ID
# ==========================================================

def generar_id_unico(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

# ==========================================================
# ================== CRUD USUARIOS (1-5) ===================
# ==========================================================

def agregar_usuario(nombre):
    if not validar_texto_no_vacio(nombre):
        print("No se permiten campos vacíos.")
        return
    
    usuarios = cargar_datos("usuarios.json")
    nuevo = {
        "id": generar_id_unico(usuarios),
        "nombre": nombre
    }
    usuarios.append(nuevo)
    guardar_datos("usuarios.json", usuarios)
    print("Usuario agregado.")

def listar_usuarios():
    usuarios = cargar_datos("usuarios.json")
    if not usuarios:
        print("No hay usuarios.")
        return
    for u in usuarios:
        print(u)

def buscar_usuario_por_id(id_usuario):
    usuarios = cargar_datos("usuarios.json")
    return next((u for u in usuarios if u["id"] == id_usuario), None)

def actualizar_usuario(id_usuario, nuevo_nombre):
    usuarios = cargar_datos("usuarios.json")
    for u in usuarios:
        if u["id"] == id_usuario:
            u["nombre"] = nuevo_nombre
            guardar_datos("usuarios.json", usuarios)
            print("Usuario actualizado.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(id_usuario):
    if usuario_tiene_prestamos_activos(id_usuario):
        print("No se puede eliminar. Tiene préstamos activos.")
        return
    
    usuarios = cargar_datos("usuarios.json")
    usuarios = [u for u in usuarios if u["id"] != id_usuario]
    guardar_datos("usuarios.json", usuarios)
    print("Usuario eliminado.")

# ==========================================================
# ================= CRUD HERRAMIENTAS (6-10) ===============
# ==========================================================

def agregar_herramienta(nombre, stock):
    if not validar_texto_no_vacio(nombre):
        print("Nombre inválido.")
        return
    if not validar_stock(stock):
        print("Stock inválido.")
        return

    herramientas = cargar_datos("herramientas.json")
    nueva = {
        "id": generar_id_unico(herramientas),
        "nombre": nombre,
        "stock": stock
    }
    herramientas.append(nueva)
    guardar_datos("herramientas.json", herramientas)
    print("Herramienta agregada.")

def listar_herramientas():
    herramientas = cargar_datos("herramientas.json")
    for h in herramientas:
        print(h)

def buscar_herramienta_por_id(id_herramienta):
    herramientas = cargar_datos("herramientas.json")
    return next((h for h in herramientas if h["id"] == id_herramienta), None)

def actualizar_herramienta(id_herramienta, nuevo_stock):
    herramientas = cargar_datos("herramientas.json")
    for h in herramientas:
        if h["id"] == id_herramienta:
            h["stock"] = nuevo_stock
            guardar_datos("herramientas.json", herramientas)
            print("Herramienta actualizada.")
            return
    print("Herramienta no encontrada.")

def eliminar_herramienta(id_herramienta):
    herramientas = cargar_datos("herramientas.json")
    herramientas = [h for h in herramientas if h["id"] != id_herramienta]
    guardar_datos("herramientas.json", herramientas)
    print("Herramienta eliminada.")

# ==========================================================
# ================== PRÉSTAMOS (11-20) =====================
# ==========================================================

def registrar_prestamo(id_usuario, id_herramienta, fecha):
    if not validar_fecha(fecha):
        print("Fecha inválida.")
        return

    herramientas = cargar_datos("herramientas.json")
    prestamos = cargar_datos("prestamos.json")

    herramienta = buscar_herramienta_por_id(id_herramienta)

    if herramienta and herramienta["stock"] > 0:
        herramienta["stock"] -= 1

        nuevo = {
            "id": generar_id_unico(prestamos),
            "id_usuario": id_usuario,
            "id_herramienta": id_herramienta,
            "fecha": fecha,
            "estado": "activo"
        }

        prestamos.append(nuevo)

        guardar_datos("herramientas.json", herramientas)
        guardar_datos("prestamos.json", prestamos)
        print("Préstamo registrado.")
    else:
        print("No hay stock disponible.")

def devolver_herramienta(id_prestamo):
    prestamos = cargar_datos("prestamos.json")
    herramientas = cargar_datos("herramientas.json")

    for p in prestamos:
        if p["id"] == id_prestamo and p["estado"] == "activo":
            p["estado"] = "devuelto"

            herramienta = buscar_herramienta_por_id(p["id_herramienta"])
            if herramienta:
                herramienta["stock"] += 1

            guardar_datos("prestamos.json", prestamos)
            guardar_datos("herramientas.json", herramientas)
            print("Devuelto correctamente.")
            return
    print("Préstamo no encontrado.")

def listar_prestamos():
    prestamos = cargar_datos("prestamos.json")
    if not prestamos:
        print("No hay préstamos.")
        return
    for p in prestamos:
        print(p)

def buscar_prestamo_por_usuario(id_usuario):
    prestamos = cargar_datos("prestamos.json")
    return [p for p in prestamos if p["id_usuario"] == id_usuario]

def calcular_dias_prestamo(fecha):
    fecha_inicio = datetime.strptime(fecha, "%d-%m-%Y")
    return (datetime.now() - fecha_inicio).days

def generar_reporte_prestamos_activos():
    prestamos = cargar_datos("prestamos.json")
    return [p for p in prestamos if p["estado"] == "activo"]

def verificar_stock_disponible(id_herramienta):
    herramienta = buscar_herramienta_por_id(id_herramienta)
    if herramienta:
        return herramienta["stock"] > 0
    return False

def contar_prestamos_activos():
    prestamos = cargar_datos("prestamos.json")
    return sum(1 for p in prestamos if p["estado"] == "activo")

def usuario_tiene_prestamos_activos(id_usuario):
    prestamos = cargar_datos("prestamos.json")
    return any(p["id_usuario"] == id_usuario and p["estado"] == "activo" for p in prestamos)

def prestamos_vencidos(dias_limite):
    prestamos = cargar_datos("prestamos.json")
    vencidos = []
    for p in prestamos:
        if p["estado"] == "activo":
            dias = calcular_dias_prestamo(p["fecha"])
            if dias > dias_limite:
                vencidos.append(p)
    return vencidos

# ==========================================================
# ================== FUNCIONES EXTRA (21-30) ===============
# ==========================================================

def herramientas_mas_prestadas():
    prestamos = cargar_datos("prestamos.json")
    conteo = {}
    for p in prestamos:
        id_h = p["id_herramienta"]
        conteo[id_h] = conteo.get(id_h, 0) + 1
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

def buscar_herramientas_sin_stock():
    herramientas = cargar_datos("herramientas.json")
    return [h for h in herramientas if h["stock"] == 0]

def total_herramientas_disponibles():
    herramientas = cargar_datos("herramientas.json")
    return sum(h["stock"] for h in herramientas)

def historial_usuario(id_usuario):
    prestamos = cargar_datos("prestamos.json")
    return [p for p in prestamos if p["id_usuario"] == id_usuario]

def cerrar_prestamos_vencidos(dias_limite):
    prestamos = cargar_datos("prestamos.json")
    cambios = False
    for p in prestamos:
        if p["estado"] == "activo":
            dias = calcular_dias_prestamo(p["fecha"])
            if dias > dias_limite:
                p["estado"] = "vencido"
                cambios = True
    if cambios:
        guardar_datos("prestamos.json", prestamos)

def extender_prestamo(id_prestamo, nueva_fecha):
    prestamos = cargar_datos("prestamos.json")
    for p in prestamos:
        if p["id"] == id_prestamo:
            p["fecha"] = nueva_fecha
            guardar_datos("prestamos.json", prestamos)
            print("Fecha extendida.")
            return
    print("Préstamo no encontrado.")

# ==========================================================
# FIN DEL SISTEMA COMPLETO
# ==========================================================

# ==========================================================
# MODULO DE MULTAS Y REPORTES ADMINISTRATIVOS
# Compatible con sistema de préstamos de herramientas
# ==========================================================

import json
from datetime import datetime

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

MULTA_POR_DIA = 2000  # Valor de multa por día de retraso

# ==========================================================
# FUNCIONES BASE
# ==========================================================

def cargar_datos(ruta):
    try:
        with open(ruta, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# ==========================================================
# CALCULAR DÍAS DE RETRASO
# ==========================================================

def calcular_dias_retraso(fecha_prestamo):
    fecha_inicio = datetime.strptime(fecha_prestamo, "%d-%m-%Y")
    hoy = datetime.now()
    return (hoy - fecha_inicio).days

# ==========================================================
# DETECTAR PRÉSTAMOS VENCIDOS
# ==========================================================

def obtener_prestamos_vencidos(dias_limite):
    prestamos = cargar_datos("prestamos.json")
    vencidos = []

    for p in prestamos:
        if p["estado"] == "activo":
            dias = calcular_dias_retraso(p["fecha"])
            if dias > dias_limite:
                vencidos.append(p)

    return vencidos

# ==========================================================
# CALCULAR MULTA DE UN PRÉSTAMO
# ==========================================================

def calcular_multa(fecha_prestamo, dias_limite):
    dias = calcular_dias_retraso(fecha_prestamo)
    if dias > dias_limite:
        dias_retraso = dias - dias_limite
        return dias_retraso * MULTA_POR_DIA
    return 0

# ==========================================================
# BLOQUEAR USUARIOS MOROSOS
# ==========================================================

def bloquear_usuarios_morosos(dias_limite):
    usuarios = cargar_datos("usuarios.json")
    prestamos = cargar_datos("prestamos.json")

    for usuario in usuarios:
        usuario["bloqueado"] = False

    for p in prestamos:
        if p["estado"] == "activo":
            dias = calcular_dias_retraso(p["fecha"])
            if dias > dias_limite:
                for u in usuarios:
                    if u["id"] == p["id_usuario"]:
                        u["bloqueado"] = True

    guardar_datos("usuarios.json", usuarios)
    print("Usuarios morosos actualizados.")

# ==========================================================
# REPORTE ADMINISTRATIVO COMPLETO
# ==========================================================

def generar_reporte_general(dias_limite):
    prestamos = cargar_datos("prestamos.json")
    herramientas = cargar_datos("herramientas.json")
    usuarios = cargar_datos("usuarios.json")

    total_prestamos = len(prestamos)
    activos = [p for p in prestamos if p["estado"] == "activo"]
    vencidos = obtener_prestamos_vencidos(dias_limite)

    herramientas_sin_stock = [h for h in herramientas if h["stock"] == 0]

    print("\n====== REPORTE ADMINISTRATIVO ======")
    print(f"Total préstamos registrados: {total_prestamos}")
    print(f"Préstamos activos: {len(activos)}")
    print(f"Préstamos vencidos: {len(vencidos)}")
    print(f"Herramientas sin stock: {len(herramientas_sin_stock)}")
    print("====================================\n")

# ==========================================================
# GENERAR REPORTE EN ARCHIVO TXT
# ==========================================================

def exportar_reporte_txt(dias_limite):
    vencidos = obtener_prestamos_vencidos(dias_limite)

    with open("reporte_morosos.txt", "w") as archivo:
        archivo.write("===== REPORTE DE PRÉSTAMOS VENCIDOS =====\n")
        for p in vencidos:
            multa = calcular_multa(p["fecha"], dias_limite)
            linea = f"Prestamo ID: {p['id']} | Usuario: {p['id_usuario']} | Multa: ${multa}\n"
            archivo.write(linea)

    print("Reporte exportado correctamente.")

# ==========================================================
# SISTEMA DE ALERTAS AL INICIAR
# ==========================================================

def mostrar_alertas(dias_limite):
    vencidos = obtener_prestamos_vencidos(dias_limite)
    herramientas = cargar_datos("herramientas.json")

    sin_stock = [h for h in herramientas if h["stock"] == 0]

    if vencidos:
        print(f"⚠ ALERTA: Hay {len(vencidos)} préstamos vencidos.")
    if sin_stock:
        print(f"⚠ ALERTA: Hay {len(sin_stock)} herramientas sin stock.")
    if not vencidos and not sin_stock:
        print("Sistema en estado normal.")

# ==========================================================
# EJECUCIÓN PRINCIPAL
# ==========================================================

if __name__ == "__main__":
    DIAS_LIMITE = 7  # Ejemplo: préstamo máximo 7 días

    mostrar_alertas(DIAS_LIMITE)
    generar_reporte_general(DIAS_LIMITE)
    bloquear_usuarios_morosos(DIAS_LIMITE)
    exportar_reporte_txt(DIAS_LIMITE)

    # ==========================================================
# SISTEMA PROFESIONAL DE REGISTRO DE EVENTOS (LOGS)
# ==========================================================

from datetime import datetime
import os

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ARCHIVO_LOG = "registro_eventos.txt"

# ==========================================================
# FUNCIÓN PRINCIPAL DE LOG
# ==========================================================

def registrar_evento(tipo, mensaje):
    """
    Registra un evento en el archivo de log.
    
    tipo: INFO | WARNING | ERROR
    mensaje: descripción del evento
    """

    fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    linea = f"[{fecha_hora}] [{tipo}] {mensaje}\n"

    with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

# ==========================================================
# FUNCIONES ESPECIALIZADAS
# ==========================================================

def log_info(mensaje):
    registrar_evento("INFO", mensaje)

def log_warning(mensaje):
    registrar_evento("WARNING", mensaje)

def log_error(mensaje):
    registrar_evento("ERROR", mensaje)

# ==========================================================
# FUNCIÓN PARA CREAR ARCHIVO SI NO EXISTE
# ==========================================================

def inicializar_log():
    if not os.path.exists(ARCHIVO_LOG):
        with open(ARCHIVO_LOG, "w", encoding="utf-8") as archivo:
            archivo.write("===== REGISTRO DE EVENTOS DEL SISTEMA =====\n\n")

            if herramienta["stock"] <= 0:
    log_error(f"Intento de préstamo sin stock. Herramienta ID: {id_herramienta}")
    print("No hay stock disponible.")
    return

if usuario.get("bloqueado", False):
    log_warning(f"Usuario bloqueado intentó prestar herramienta. Usuario ID: {id_usuario}")
    print("Usuario bloqueado.")
    return

if not validar_fecha(fecha):
    log_error(f"Fecha inválida ingresada: {fecha}")
    print("Fecha inválida.")
    return

log_info(f"Usuario eliminado. ID: {id_usuario}")


"""

===== REGISTRO DE EVENTOS DEL SISTEMA =====

[19-02-2026 09:15:22] [INFO] Préstamo registrado. Usuario ID: 3, Herramienta ID: 5
[19-02-2026 09:20:10] [ERROR] Intento de préstamo sin stock. Herramienta ID: 2
[19-02-2026 09:25:33] [WARNING] Usuario bloqueado intentó prestar herramienta. Usuario ID: 4
[19-02-2026 09:30:02] [ERROR] Fecha inválida ingresada: 31-02-2026

"""