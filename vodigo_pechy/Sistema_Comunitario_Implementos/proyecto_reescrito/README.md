# Sistema de Gestión Comunitaria de Implementos

## Descripción
Sistema desarrollado en Python para la gestión de préstamos de herramientas e implementos en comunidades vecinales. Funciona completamente en consola y permite controlar inventario, usuarios y asignaciones de manera eficiente.

## Características Principales

### Módulos del Sistema
- **Gestión de Implementos**: Control completo del inventario (crear, modificar, eliminar, consultar)
- **Gestión de Miembros**: Administración de residentes y administradores
- **Gestión de Asignaciones**: Control de préstamos, devoluciones y extensiones
- **Reportes y Consultas**: Estadísticas y análisis del sistema

### Funcionalidades

#### Para Administradores
- Registrar y administrar implementos
- Gestionar miembros de la comunidad
- Crear y controlar asignaciones
- Procesar devoluciones y cancelaciones
- Generar reportes detallados
- Ver asignaciones vencidas

#### Para Residentes
- Consultar implementos disponibles
- Ver asignaciones personales activas
- Consultar estado de implementos específicos
- Revisar historial personal de préstamos

### Características Técnicas
- **Persistencia Multi-formato**: Datos guardados en TXT, JSON y CSV
- **Sistema de Logs**: Registro automático de eventos en múltiples formatos
- **Validaciones**: Control de stock, fechas y datos duplicados
- **Arquitectura OOP**: Código organizado en clases y módulos

## Estructura del Proyecto

```
proyecto_reescrito/
├── nucleo_sistema.py           # Clases base y utilidades
├── modulo_implementos.py       # Gestión de inventario
├── modulo_miembros.py          # Gestión de usuarios
├── modulo_asignaciones.py      # Modelo de asignaciones
├── interfaz_asignaciones.py    # Interfaz para préstamos
├── modulo_reportes.py          # Generación de reportes
├── sistema_principal.py        # Archivo principal ejecutable
└── README.md                   # Este archivo
```

### Archivos de Datos (creados automáticamente)
- `inventario.txt` / `.json` / `.csv`
- `miembros.txt` / `.json` / `.csv`
- `asignaciones.txt` / `.json` / `.csv`
- `eventos_sistema.txt` / `.json` / `.csv`

## Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS
- Editor recomendado: Visual Studio Code

## Instrucciones de Instalación y Ejecución

### 1. Preparación
```bash
# Clonar o descargar el proyecto
# Navegar al directorio del proyecto
cd proyecto_reescrito
```

### 2. Ejecución
```bash
# Método 1: Ejecutar desde terminal
python3 sistema_principal.py

# Método 2: Ejecutar en Visual Studio Code
# Abrir sistema_principal.py y presionar F5
```

### 3. Primer Uso
Al iniciar el sistema por primera vez:
1. Los archivos de datos se crearán automáticamente
2. Recomendamos crear primero algunos miembros administradores
3. Luego registrar implementos en el inventario
4. Finalmente comenzar a gestionar asignaciones

## Guía de Uso Rápida

### Flujo Típico de Trabajo

1. **Configuración Inicial (Administrador)**
   - Acceder al Panel de Administración
   - Crear miembros (residentes y administradores)
   - Registrar implementos en el inventario

2. **Operación Diaria (Administrador)**
   - Crear asignaciones cuando un residente solicita un implemento
   - Procesar devoluciones
   - Consultar reportes de stock y asignaciones vencidas

3. **Consultas (Residente)**
   - Ver catálogo de implementos disponibles
   - Consultar asignaciones activas personales
   - Revisar historial de préstamos

## Datos de Ejemplo

### Estructura de un Implemento
```
ID: TALADRO01
Nombre: Taladro percutor industrial
Categoría: construcción
Stock: 2
Condición: disponible
Valor: 350000.00
```

### Estructura de un Miembro
```
Código: RES001
Nombres: Juan Carlos
Apellidos: González Pérez
Teléfono: 3001234567
Dirección: Calle 45 #12-34
Rol: residente
```

### Estructura de una Asignación
```
ID: ASG001
Miembro: RES001
Implemento: TALADRO01
Cantidad: 1
Fecha salida: 2026-02-14
Fecha retorno: 2026-02-21
Estado: activo
```

## Reportes Disponibles

1. **Implementos con Stock Crítico**: Muestra items con menos de 3 unidades
2. **Asignaciones Vigentes**: Lista todos los préstamos activos
3. **Asignaciones Vencidas**: Identifica préstamos no devueltos a tiempo
4. **Historial por Miembro**: Registro completo de asignaciones de un residente
5. **Implementos Populares**: Ranking de los más solicitados
6. **Miembros Activos**: Usuarios con más asignaciones

## Sistema de Logs

Todos los eventos importantes quedan registrados automáticamente:
- **Acciones**: Creaciones, actualizaciones, eliminaciones exitosas
- **Errores**: Intentos fallidos, validaciones, problemas de stock
- **Advertencias**: Situaciones que requieren atención

Los logs se guardan en tres formatos para facilitar análisis:
- `eventos_sistema.txt` - Lectura humana
- `eventos_sistema.json` - Procesamiento automatizado
- `eventos_sistema.csv` - Análisis en hojas de cálculo

## Solución de Problemas

### El sistema no inicia
- Verificar que Python esté instalado correctamente
- Asegurar que todos los archivos .py estén en el mismo directorio

### Error al guardar datos
- Verificar permisos de escritura en el directorio
- Asegurar que no haya archivos bloqueados por otros programas

### No se ven los datos guardados
- Los datos solo aparecen después de usar la opción "Guardar"
- Revisar que los archivos .txt, .json y .csv estén en el directorio

## Buenas Prácticas

1. **Guardar Frecuentemente**: Use la opción de guardar antes de salir de cada módulo
2. **Revisar Vencidos**: Consulte regularmente las asignaciones vencidas
3. **Mantener Stock**: Revise el reporte de stock crítico semanalmente
4. **Logs**: Revise los logs periódicamente para detectar problemas
5. **Respaldos**: Haga copias de seguridad de los archivos de datos

## Diferencias con Versiones Anteriores

Este sistema ha sido completamente reescrito con:
- Arquitectura orientada a objetos
- Nombres de variables y funciones en estilo diferente
- Estructura modular mejorada
- Interfaz de usuario renovada
- Mayor robustez en manejo de errores

## Soporte y Contacto

Para reportar problemas o sugerencias:
- Revise primero la documentación
- Consulte los logs del sistema
- Verifique que los archivos estén completos

## Licencia

Este sistema es de uso libre para comunidades y organizaciones vecinales.

---

**Versión**: 2.0
**Última actualización**: Febrero 2026
**Desarrollado para**: Gestión comunitaria de recursos compartidos
