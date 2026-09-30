from abc import ABC, abstractmethod
from core.config_manager import ConfigManager

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandNew(ICommand):
    def __init__(self, receptor, nombre):
        self.receptor = receptor
        self.nombre = nombre
    def execute(self):
        self.receptor.crear_archivo(self.nombre)

class CommandList(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.listar_archivos()

class CommandSwitch(ICommand):
    def __init__(self, receptor, nombre):
        self.receptor = receptor
        self.nombre = nombre
    def execute(self):
        self.receptor.cambiar_archivo_activo(self.nombre)

class CommandDelete(ICommand):
    def __init__(self, receptor, nombre):
        self.receptor = receptor
        self.nombre = nombre
    def execute(self):
        self.receptor.eliminar_archivo(self.nombre)

class CommandWrite(ICommand):
    def __init__(self, receptor, texto):
        self.receptor = receptor
        self.texto = texto
    def execute(self):
        self.receptor.escribir_en_activo(self.texto)

class CommandConfig(ICommand):
    def __init__(self, ruta):
        self.ruta = ruta
    def execute(self):
        ConfigManager.cargar_configuracion(self.ruta)

class CommandShow(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.mostrar_codigo()

class CommandUndo(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.deshacer()

class CommandRedo(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.rehacer()

class CommandCheck(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.verificar_sintaxis()

class CommandSort(ICommand):
    def __init__(self, receptor, criterio, algoritmo):
        self.receptor = receptor
        self.criterio = criterio
        self.algoritmo = algoritmo
    def execute(self):
        self.receptor.ordenar_diagnosticos(self.criterio, self.algoritmo)

class CommandAnalyze(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.encolar_peticion_ia()

class CommandQueueStatus(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.mostrar_estado_cola()

class CommandProcess(ICommand):
    def __init__(self, receptor):
        self.receptor = receptor
    def execute(self):
        self.receptor.procesar_cola_ia()

class CommandHelp(ICommand):
    def execute(self):
        print("\n--- COMANDOS DISPONIBLES EN SYNTHETIX STUDIO ---")
        print(" help                : Muestra esta lista de comandos.")
        print(" config <archivo>    : Carga la URL de la API (ej. config config.txt).")
        print(" new <nombre>        : Crea un nuevo archivo y lo pone activo.")
        print(" switch <nombre>     : Cambia a otro archivo abierto.")
        print(" list                : Muestra todos los archivos abiertos.")
        print(" delete <nombre>     : Elimina un archivo.")
        print(" write <texto>       : Agrega una linea al archivo activo.")
        print(" show                : Muestra el codigo del archivo activo.")
        print(" undo                : Deshace el ultimo 'write' (LIFO).")
        print(" redo                : Rehace el ultimo 'undo' (LIFO).")
        print(" check               : Revisa llaves y corchetes abiertos (Sintaxis).")
        print(" sort <crit> <algo>  : Ordena errores (ej. sort line mergesort).")
        print(" analyze             : Encola el archivo activo (Buffer FIFO).")
        print(" queue-status        : Muestra el estado del Buffer FIFO.")
        print(" process             : Desencola y envia a internet (HTTP POST).")
        print(" exit / salir        : Cierra la aplicacion.")
        print("------------------------------------------------")