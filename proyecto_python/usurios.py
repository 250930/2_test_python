import json
from datos import registro_eventos

def agregar_usuario():
    try:
        with open("usuarios.json", "r") as arch:
            datos = json.load(arch)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = []

    id_usuario = max([u["id"] for u in datos], default=0) + 1

    nombre = input("Ingrese el nombre del usuario: ")
    apellidos = input("Ingrese sus apellidos: ")
    numero = input("Ingrese el número telefónico: ")
    direccion = input("Ingrese su dirección: ")

    while True:
        try:
            tipo_op = int(input("""
Ingrese el tipo de usuario:
1. Administrador
2. Residente
Seleccione: """))

            if tipo_op == 1:
                tipo_usuario = "administrador"
                break
            elif tipo_op == 2:
                tipo_usuario = "residente"
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número válido.")

    nuevo_usuario = {
        "id": id_usuario,
        "nombres": nombre,
        "apellidos": apellidos,
        "telefono": numero,
        "direccion": direccion,
        "tipo_usuario": tipo_usuario
    }

    datos.append(nuevo_usuario)

    with open("usuarios.json", "w") as arch:
        json.dump(datos, arch, indent=4)

    registro_eventos(f"Usuario ID {id_usuario} agregado correctamente.")
    print("Usuario agregado exitosamente.")

def eliminar_usuario(id_usuario):
    try:
        with open("usuarios.json", "r") as arch:
                datos = json.load(arch)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: No se pudo leer el archivo o el archivo no existe.")
        return
    usuario_encontrado = None
    for usuarios in datos:
        if usuarios["id"] == id_usuario:
            usuario_encontrado = usuarios
            break
    
    if usuario_encontrado is None:
        print(f"El ID: {id_usuario} no existe")
        return

    datos.remove(usuario_encontrado)
    
    with open("usuarios.json", "w") as arch:
        json.dump(datos, arch, indent=4)
    print(f"El usuario con el ID {id_usuario} fue eliminada correctamente")
    registro_eventos(f"Usuario ID {id_usuario} eliminado.")
    print("Usuario eliminado correctamente.")
def actualizar_usuario():
    with open("usuarios.json", "r") as arch:
        datos = json.load(arch)

    id_usuario = int(input("Ingrese el ID del usuario que desea modificar: "))

    for usuario in datos:
        if usuario["id"] == id_usuario:
            print("Ingrese los nuevos datos del usuario (deje en blanco para mantener el valor actual):")

            nombres = input(f"Nombres ({usuario['nombres']}): ") or usuario['nombres']
            apellidos = input(f"Apellidos ({usuario['apellidos']}): ") or usuario['apellidos']
            telefono = input(f"Teléfono ({usuario['telefono']}): ") or usuario['telefono']
            direccion = input(f"Dirección ({usuario['direccion']}): ") or usuario['direccion']
            tipo_input = input(f"""
                Actualizar tipo de usuario ({usuario['tipo_usuario']})
                1. administrador
                2. residente
                Deje en blanco para mantener el actual:
                """)

            if tipo_input == "":
                    tipo_usuario = usuario["tipo_usuario"]
            else:
                    while tipo_input not in ["1", "2"]:
                        print("Opción no válida.")
                        tipo_input = input("Ingrese 1 o 2: ")

                    if tipo_input == "1":
                        tipo_usuario = "administrador"
                    else:
                        tipo_usuario = "residente"

            usuario.update({
                    "id": id_usuario,
                    "nombres": nombres,
                    "apellidos": apellidos,
                    "telefono": telefono,
                    "direccion": direccion,
                    "tipo_usuario": tipo_usuario
                    })

            with open("usuarios.json", "w") as arch:
                json.dump(datos, arch, indent=4)

            print("Usuario modificado exitosamente.")
            return

    print("Usuario no encontrado.") 
    registro_eventos(f"Intento fallido de actualizar usuario ID {id_usuario}.")