SISTEMA DE GESTIÓN DE USUARIOS Y HERRAMIENTAS

DESCRIPCIÓN GENERAL

Este proyecto es un sistema desarrollado en Python que permite
administrar usuarios y herramientas mediante una interfaz en consola. El
sistema implementa operaciones CRUD (Crear, Leer, Actualizar y Eliminar)
y utiliza archivos en formato JSON para almacenar la información de
manera persistente.

El objetivo principal del proyecto es aplicar los fundamentos de
programación, el uso de estructuras de datos dinámicas como listas y
diccionarios, la modularización del código y la separación de
responsabilidades.

ARQUITECTURA DEL SISTEMA

El sistema está organizado en módulos para mantener una estructura clara
y ordenada:

1.  MÓDULO MENÚ Controla el flujo del programa.
    -   Muestra las opciones disponibles.
    -   Captura la opción seleccionada por el usuario.
    -   Redirige la ejecución hacia el módulo correspondiente.
    -   Utiliza un ciclo while True para mantener el sistema activo.
    -   Finaliza con break cuando el usuario decide salir.
2.  MÓDULO DATOS Gestiona la persistencia de la información.
    -   Usa json.load() para deserializar datos del archivo JSON a
        estructuras Python.
    -   Usa json.dump() para serializar estructuras Python nuevamente a
        formato JSON.
    -   Se encarga únicamente de leer y guardar información.
3.  MÓDULO USUARIOS Implementa la gestión completa de usuarios.
    -   Agregar usuario: crea un diccionario con los datos ingresados y
        lo añade a la lista.
    -   Listar usuarios: recorre la lista y muestra la información
        almacenada.
    -   Actualizar usuario: busca por ID y modifica directamente los
        valores del diccionario.
    -   Eliminar usuario: busca por ID y elimina el registro usando
        remove().
4.  MÓDULO HERRAMIENTAS Funciona con la misma lógica estructural que
    usuarios, pero aplicado a la entidad herramienta.
    -   Agregar herramienta.
    -   Listar herramientas.
    -   Actualizar herramienta.
    -   Eliminar herramienta.
5.  MÓDULO REPORTES Genera información estadística básica.
    -   Conteo total de registros.
    -   Clasificación por tipo o estado.
    -   Uso de contadores y recorridos sobre listas en memoria.

PERSISTENCIA DE DATOS

El sistema utiliza archivos JSON como mecanismo de almacenamiento. Esto
permite que la información permanezca guardada incluso después de cerrar
el programa.

Proceso técnico: - JSON -> json.load() -> Lista en memoria - Lista en
memoria -> json.dump() -> JSON

COMPLEJIDAD

Las operaciones de búsqueda (actualizar y eliminar) tienen una
complejidad O(n), ya que recorren la lista hasta encontrar coincidencia.

CONCEPTOS APLICADOS

-   Modularización del código
-   Separación de responsabilidades
-   Manipulación de listas y diccionarios
-   Estructuras de datos mutables
-   Serialización y deserialización JSON
-   Control de flujo con ciclos y condicionales
-   Implementación completa de un sistema CRUD

AUTOR

Proyecto académico desarrollado para aplicar fundamentos de programación
en Python y gestión básica de datos.
