from menu import menu_principal
from funciones import grilla

def main():
    lineup = grilla()
    codigos = []
    nombre_artistas = []
    tot = 0
    venta_tot = 0
    vendidas_gen = 0
    vendidas_vip = 0
    escenarios_rankeados = [0, 0, 0, 0, 0]
    menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

main()

