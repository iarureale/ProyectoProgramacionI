from menu import menu_principal
from funciones import grilla, leer_archivo

def main():
    config = leer_archivo()
    lineup = grilla()
    codigos = []
    nombre_artistas = []
    tot = 0
    venta_tot = 0
    vendidas_gen = 0
    vendidas_vip = 0

    menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, config)

main()

