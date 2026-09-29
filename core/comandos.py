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

# (Pon esto debajo de CommandConfig en core/comandos.py)

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