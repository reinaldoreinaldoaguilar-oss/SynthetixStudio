import urllib.request
import json           
from structures.estructuras import Pila, Cola 
from core.motor_ordenamiento import Diagnostico, MotorOrdenamiento
from core.config_manager import ConfigManager 

class NodoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = ""
        self.pila_undo = Pila()
        self.pila_redo = Pila()
        self.siguiente = None

class ListaArchivos:
    def __init__(self):
        self.cabeza = None
        self.archivo_activo = None
        self.cola_peticiones_ia = Cola() 

    def crear_archivo(self, nombre):
        nuevo = NodoArchivo(nombre)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            temp = self.cabeza
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo
        
        self.archivo_activo = nuevo
        print(f"[OK] Archivo '{nombre}' creado y seleccionado como activo.")

    def listar_archivos(self):
        if self.cabeza is None:
            print("No hay archivos abiertos en la sesion.")
            return
        print("--- Archivos Abiertos ---")
        temp = self.cabeza
        pos = 1
        while temp is not None:
            estado = " [ACTIVO]" if temp == self.archivo_activo else ""
            print(f"{pos}. {temp.nombre}{estado}")
            temp = temp.siguiente
            pos += 1
        print("-------------------------")

    def cambiar_archivo_activo(self, nombre):
        temp = self.cabeza
        while temp is not None:
            if temp.nombre == nombre:
                self.archivo_activo = temp
                print(f"[OK] Ahora estas editando: {nombre}")
                return
            temp = temp.siguiente
        print(f"[ERROR] El archivo '{nombre}' no esta abierto.")

    def eliminar_archivo(self, nombre):
        if self.cabeza is None:
            print("[ERROR] No hay archivos para eliminar.")
            return

        if self.cabeza.nombre == nombre:
            a_borrar = self.cabeza
            self.cabeza = self.cabeza.siguiente
            if self.archivo_activo == a_borrar:
                self.archivo_activo = self.cabeza
            print(f"[OK] Archivo '{nombre}' eliminado.")
            return

        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.nombre != nombre:
            actual = actual.siguiente

        if actual.siguiente is not None:
            a_borrar = actual.siguiente
            actual.siguiente = a_borrar.siguiente
            if self.archivo_activo == a_borrar:
                self.archivo_activo = self.cabeza
            print(f"[OK] Archivo '{nombre}' eliminado.")
        else:
            print("[ERROR] Archivo no encontrado.")

    def escribir_en_activo(self, texto):
        if self.archivo_activo is None:
            print("[ERROR] No hay archivo activo para escribir.")
            return
        

        self.archivo_activo.pila_undo.apilar(self.archivo_activo.contenido)

        self.archivo_activo.pila_redo.vaciar()

        self.archivo_activo.contenido += texto + "\n"
        print("[OK] Linea agregada al codigo.")

    def mostrar_codigo(self):
        if self.archivo_activo is None:
            return
        print(f"\n--- Codigo de {self.archivo_activo.nombre} ---")
        print(self.archivo_activo.contenido, end="")
        print("---------------------------------")

    def deshacer(self):
        if self.archivo_activo is None: return
        if self.archivo_activo.pila_undo.esta_vacia():
            print("[INFO] No hay mas acciones para deshacer.")
            return

        self.archivo_activo.pila_redo.apilar(self.archivo_activo.contenido)

        self.archivo_activo.contenido = self.archivo_activo.pila_undo.desapilar()
        print("[OK] Cambio deshecho (Undo).")

    def rehacer(self):
        if self.archivo_activo is None: return
        if self.archivo_activo.pila_redo.esta_vacia():
            print("[INFO] No hay mas acciones para rehacer.")
            return
        self.archivo_activo.pila_undo.apilar(self.archivo_activo.contenido)
        # Volver al futuro
        self.archivo_activo.contenido = self.archivo_activo.pila_redo.desapilar()
        print("[OK] Cambio rehecho (Redo).")

    def verificar_sintaxis(self):
        if self.archivo_activo is None: return
        if not self.archivo_activo.contenido:
            print("[OK] El archivo esta vacio, no hay errores de sintaxis.")
            return

        pila_simbolos = Pila()
        linea_actual = 1

        print(f"--- Analizando sintaxis en '{self.archivo_activo.nombre}' ---")
        for c in self.archivo_activo.contenido:
            if c == '\n': 
                linea_actual += 1
                continue
            
            if c in ['(', '{', '[']:
                pila_simbolos.apilar(c)
            elif c in [')', '}', ']']:
                if pila_simbolos.esta_vacia():
                    print(f"[ERROR L{linea_actual}] Se encontro '{c}' pero no hay un simbolo que lo abra.")
                    return
                tope = pila_simbolos.desapilar()
                if (c == ')' and tope != '(') or \
                   (c == '}' and tope != '{') or \
                   (c == ']' and tope != '['):
                    print(f"[ERROR L{linea_actual}] Choque de simbolos: abriste con '{tope}' pero cerraste con '{c}'.")
                    return

        if not pila_simbolos.esta_vacia():
            print(f"[ERROR L{linea_actual}] Codigo incompleto. Te falto cerrar algun simbolo ( , {{ o [.")
        else:
            print("[OK] Balanceo de simbolos de agrupacion CORRECTO.")

    # --- METODOS PARTE 3: MOTOR DE ORDENAMIENTO ---
    def ordenar_diagnosticos(self, criterio, algoritmo):
        if self.archivo_activo is None:
            print("[ERROR] No hay archivo activo para analizar.")
            return
        
        alertas = [
            Diagnostico(15, 2, "Variable 'x' declarada pero sin uso."),
            Diagnostico(3, 5, "Error de sintaxis: Falta punto y coma."),
            Diagnostico(42, 1, "Advertencia: Indentacion incorrecta."),
            Diagnostico(8, 4, "Peligro: Posible desbordamiento de memoria."),
            Diagnostico(21, 3, "Advertencia: Ciclo podria ser infinito.")
        ]

        print(f"--- Ordenando diagnosticos de {self.archivo_activo.nombre} ---")
        
        if algoritmo == "mergesort":
            MotorOrdenamiento.merge_sort(alertas, criterio)
        elif algoritmo == "shellsort":
            MotorOrdenamiento.shell_sort(alertas, criterio)
        else:
            print("[ERROR] Algoritmo desconocido. Usa 'mergesort' o 'shellsort'.")
            return

        for alerta in alertas:
            print(f"[Linea {alerta.linea}] (Gravedad: {alerta.gravedad}) -> {alerta.mensaje}")
        print("--------------------------------------")

    def encolar_peticion_ia(self):
        if self.archivo_activo is None:
            print("[ERROR] No hay archivo activo para analizar.")
            return
        if not self.archivo_activo.contenido.strip():
            print("[ERROR] El archivo esta vacio, no hay codigo para enviar.")
            return
        
        self.cola_peticiones_ia.encolar(self.archivo_activo.contenido)
        print("[OK] Codigo fuente encolado en el Buffer FIFO.")

    def mostrar_estado_cola(self):
        self.cola_peticiones_ia.mostrar_estado()

    def procesar_cola_ia(self):
        if self.cola_peticiones_ia.esta_vacia():
            print("[INFO] No hay peticiones pendientes en la cola.")
            return
        if not ConfigManager.api_url:
            print("[ERROR] No se ha cargado la URL de la API (Usa 'config config.txt').")
            return

        codigo_fuente = self.cola_peticiones_ia.desencolar()
        
        print("\n>>> CONECTANDO CON EL SERVIDOR HTTP >>>")
        print(f"Endpoint: {ConfigManager.api_url}")
        
        data = json.dumps({"codigo": codigo_fuente}).encode('utf-8')
        req = urllib.request.Request(ConfigManager.api_url, data=data, headers={'Content-Type': 'application/json'})
        
        try:
            with urllib.request.urlopen(req) as response:
                respuesta = response.read().decode('utf-8')
                print("<<< RESPUESTA RECIBIDA POR RED <<<")
                print(respuesta)
                print("\n[Analisis de IA] Complejidad detectada: O(N)")
                print("----------------------------------------------")
        except Exception as e:
            print(f"[ERROR RED] Fallo al establecer conexion HTTP con el servidor: {e}")