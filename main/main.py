from menu import menu_principal
from funciones import grilla, leer_archivo, verificar_login, calcular_total


def main():
    """
    Carga la configuración, verifica que exista login.txt, crea el lineup vacío y las listas de artistas,
    y lanza el menú principal. Si falta un archivo obligatorio, informa el error y no inicia.
    """
    config = leer_archivo()
    if config is None: # Para que el programa no se rompa en menú en caso de no poder abrir el archivo.
        return
    if not verificar_login():
        return
    calcular_total(mostrar_avisos=True)
    lineup = grilla()
    codigos = []
    nombre_artistas = []

    menu_principal(lineup, nombre_artistas, codigos, config)

if __name__ == "__main__":
    main()