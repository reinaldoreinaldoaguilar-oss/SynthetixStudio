# Synthetix Studio - Python Edition (Mini IDE)

Synthetix Studio es un entorno de desarrollo minimalista basado en una Interfaz de Línea de Comandos (CLI). Está desarrollado en Python puro aplicando Programación Orientada a Objetos (POO) y el **Patrón de Diseño Command**. 

**Nota importante:** En estricto cumplimiento con los requerimientos, este proyecto **NO utiliza estructuras predefinidas** de Python (como listas `[]` nativas para las estructuras de datos) ni métodos de ordenamiento nativos (`.sort()`). Todas las Listas Enlazadas, Pilas y Colas fueron construidas desde cero mediante un sistema de Nodos.

## 🛠️ Ejecución del Proyecto

**1. Requisitos:**
- Python 3.x instalado en el sistema.
- No requiere librerías externas (solo módulos nativos como `os`, `json` y `urllib`).

**2. Iniciar el entorno:**
Desde la raíz del proyecto, ejecuta en la terminal:
`python main.py`

**3. Cargar configuración inicial:**
Una vez dentro del CLI, es obligatorio cargar el archivo de configuración para establecer las rutas y la URL de la API:
`Synthetix> config config.txt`

## 🏗️ Arquitectura del Sistema
El sistema respeta los principios SOLID mediante el **Command Pattern**:
- **Invoker:** El bucle principal (`main.py`) lee el input del usuario.
- **Receiver:** La clase `ListaArchivos` ejecuta la lógica de negocio y manipula las estructuras de datos.
- **Command:** Clases en `core/comandos.py` que aíslan cada orden del sistema (`CommandNew`, `CommandUndo`, `CommandProcess`, etc.).