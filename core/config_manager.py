import os

class ConfigManager:
    api_url = ""

    @staticmethod
    def cargar_configuracion(ruta_archivo):
        if not os.path.exists(ruta_archivo):
            print(f"[ERROR] No se pudo encontrar el archivo: {ruta_archivo}")
            return

        print("--- Cargando Configuracion ---")
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    print(f"[CONFIG] {linea}")
                    if "API_URL=" in linea:
                        ConfigManager.api_url = linea.split("=")[1]
        print("------------------------------")