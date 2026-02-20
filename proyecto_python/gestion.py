
import json


def cargar_archivos(nom_archivo="herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
