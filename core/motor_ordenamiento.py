class Diagnostico:
    def __init__(self, linea, gravedad, mensaje):
        self.linea = linea
        self.gravedad = gravedad
        self.mensaje = mensaje

class MotorOrdenamiento:
    @staticmethod
    def merge_sort(arreglo, criterio):
        if len(arreglo) > 1:
            medio = len(arreglo) // 2
            mitad_izq = arreglo[:medio]
            mitad_der = arreglo[medio:]

            MotorOrdenamiento.merge_sort(mitad_izq, criterio)
            MotorOrdenamiento.merge_sort(mitad_der, criterio)

            i = j = k = 0
            while i < len(mitad_izq) and j < len(mitad_der):
                if criterio == "line":
                    condicion = mitad_izq[i].linea < mitad_der[j].linea
                else: # gravedad (mayor a menor)
                    condicion = mitad_izq[i].gravedad > mitad_der[j].gravedad 

                if condicion:
                    arreglo[k] = mitad_izq[i]
                    i += 1
                else:
                    arreglo[k] = mitad_der[j]
                    j += 1
                k += 1

            while i < len(mitad_izq):
                arreglo[k] = mitad_izq[i]
                i += 1
                k += 1

            while j < len(mitad_der):
                arreglo[k] = mitad_der[j]
                j += 1
                k += 1

    @staticmethod
    def shell_sort(arreglo, criterio):
        n = len(arreglo)
        brecha = n // 2
        while brecha > 0:
            for i in range(brecha, n):
                temp = arreglo[i]
                j = i
                
                if criterio == "line":
                    while j >= brecha and arreglo[j - brecha].linea > temp.linea:
                        arreglo[j] = arreglo[j - brecha]
                        j -= brecha
                else: # gravedad
                    while j >= brecha and arreglo[j - brecha].gravedad < temp.gravedad:
                        arreglo[j] = arreglo[j - brecha]
                        j -= brecha
                        
                arreglo[j] = temp
            brecha //= 2