from menu import menu_principal
from funciones import grilla, leer_archivo

def main():
    config = leer_archivo()
    if config is None: # Para que el programa no se rompa en menú en caso de no poder abrir el archivo.
        return
    lineup = grilla()
    codigos = []
    nombre_artistas = []

    menu_principal(lineup, nombre_artistas, codigos, config)

main()

