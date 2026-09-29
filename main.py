from structures.lista_archivos import ListaArchivos
from core.comandos import (
    CommandNew, CommandList, CommandSwitch, 
    CommandDelete, CommandWrite, CommandConfig,
    CommandShow, CommandUndo, CommandRedo, CommandCheck,
    CommandSort, CommandAnalyze, CommandQueueStatus, CommandProcess # <--- TODO AÑADIDO
)

def main():
    gestor_archivos = ListaArchivos()
    print("=== Bienvenido a Synthetix Studio (Python Edition) ===")

    while True:
        try:
            entrada = input("\nSynthetix> ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if entrada.lower() in ["exit", "salir"]:
            break
        if not entrada:
            continue

        partes = entrada.split(" ", 1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        cmd = None

        if comando == "new" and argumento:
            cmd = CommandNew(gestor_archivos, argumento)
        elif comando == "list":
            cmd = CommandList(gestor_archivos)
        elif comando == "switch" and argumento:
            cmd = CommandSwitch(gestor_archivos, argumento)
        elif comando == "delete" and argumento:
            cmd = CommandDelete(gestor_archivos, argumento)
        elif comando == "config" and argumento:
            cmd = CommandConfig(argumento)
        elif comando == "write" and argumento:
            cmd = CommandWrite(gestor_archivos, argumento)
        elif comando == "show":
            cmd = CommandShow(gestor_archivos)
        elif comando == "undo":
            cmd = CommandUndo(gestor_archivos)
        elif comando == "redo":
            cmd = CommandRedo(gestor_archivos)
        elif comando == "check":
            cmd = CommandCheck(gestor_archivos)
        elif comando == "sort":
            partes_arg = argumento.split(" ")
            if len(partes_arg) == 2:
                cmd = CommandSort(gestor_archivos, partes_arg[0], partes_arg[1])
            else:
                print("[ERROR] Faltan parametros. Uso: sort <criterio> <algoritmo>")
                
        # ---> NUEVOS COMANDOS PARTE 4 Y 5 <---
        elif comando == "analyze":
            cmd = CommandAnalyze(gestor_archivos)
        elif comando == "queue-status":
            cmd = CommandQueueStatus(gestor_archivos)
        elif comando == "process":
            cmd = CommandProcess(gestor_archivos)
        # ---------------------------------------
        
        else:
            print("[ERROR] Comando no reconocido o faltan argumentos.")

        if cmd:
            cmd.execute()

if __name__ == "__main__":
    main()