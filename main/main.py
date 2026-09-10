import menu
import funciones

def main():
    lineup = funciones.grilla()
    codigos = []
    nombre_artistas = []
    tot = 0
    venta_tot = 0
    vendidas_gen = 0
    vendidas_vip = 0

    artistas_ordenados = sorted(nombre_artistas, key=str.lower) # Usamos key ya que sorted no distingue bien mayúsculas y minúsculas.
 
    menu.menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)

main()

