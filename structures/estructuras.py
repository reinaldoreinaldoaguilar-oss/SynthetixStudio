class NodoEstructura:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nuevo_nodo = NodoEstructura(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None

    def vaciar(self):
        self.tope = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def encolar(self, dato):
        nuevo_nodo = NodoEstructura(dato)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return dato

    def esta_vacia(self):
        return self.frente is None

    def mostrar_estado(self):
        if self.esta_vacia():
            print("[INFO] La cola de peticiones a la API esta vacia.")
            return
        print(f"--- Estado de la Cola FIFO (Pendientes: {self.tamano}) ---")
        actual = self.frente
        pos = 1
        while actual is not None:
            print(f"{pos}. {actual.dato}")
            actual = actual.siguiente
            pos += 1
        print("----------------------------------------------")