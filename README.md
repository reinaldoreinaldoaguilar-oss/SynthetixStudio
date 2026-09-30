# 💻 Synthetix Studio - Python Edition (Mini IDE)

Synthetix Studio es un entorno de desarrollo minimalista basado en una Interfaz de Línea de Comandos (CLI). Está desarrollado íntegramente en Python aplicando **Programación Orientada a Objetos (POO)** y el **Patrón de Diseño Command**.

> **⚠️ NOTA ACADÉMICA IMPORTANTE:** 
> En estricto cumplimiento con los requerimientos de la asignatura, este proyecto **NO utiliza estructuras predefinidas** de Python (como listas `[]` nativas) ni métodos de ordenamiento nativos (`.sort()`). Todas las Listas Enlazadas, Pilas y Colas fueron construidas desde cero mediante un sistema de Nodos referenciados en memoria.

---

## ✨ Características Principales

- **Gestión de Memoria:** Manejo de múltiples archivos simultáneos a través de una *Lista Enlazada* personalizada.
- **Historial Aislado (Undo/Redo):** Implementado mediante *Pilas (LIFO)* independientes para cada nodo de archivo.
- **Analizador Sintáctico:** Verificación de balanceo de llaves `{}`, corchetes `[]` y paréntesis `()` utilizando Pilas.
- **Motor de Ordenamiento Algorítmico:** Diagnósticos ordenados desde cero utilizando algoritmos de *MergeSort* ($O(N \log N)$) y *ShellSort*.
- **Conexión de Red (API REST):** Envío de código a un servidor HTTP externo encolando las peticiones de forma estricta mediante una *Cola (FIFO)* y procesándolas con la librería nativa `urllib`.

---

## 🏗️ Arquitectura del Sistema (Command Pattern)

El sistema respeta los principios SOLID desacoplando la interfaz del usuario de la lógica de negocio:
- **Invoker (`main.py`):** Bucle principal que recibe el input del usuario.
- **Commands (`core/comandos.py`):** Clases individuales que encapsulan cada orden.
- **Receiver (`structures/lista_archivos.py`):** Ejecuta la lógica pesada y manipula los TDA.

---

## 🚀 Instalación y Ejecución

**1. Requisitos:**
- Python 3.x instalado en el sistema.
- No requiere librerías externas (solo módulos nativos).

**2. Iniciar el entorno:**
Desde la raíz del proyecto, abre la terminal y ejecuta:
```bash
python main.py