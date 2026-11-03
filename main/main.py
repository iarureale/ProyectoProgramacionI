from menu import menu_principal
from funciones import grilla, leer_archivo

def main():
    config = leer_archivo()
    lineup = grilla()
    codigos = []
    nombre_artistas = []

    menu_principal(lineup, nombre_artistas, codigos, config)

main()

