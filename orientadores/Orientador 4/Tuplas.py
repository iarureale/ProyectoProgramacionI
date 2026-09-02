dias_habiles = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
tupla_vacia = ()
un_elemento = ("Python",)
registro = (1052, "Ana Pérez", 8.5)

# print(type(dias_habiles))
# print(type(tupla_vacia))
# print(type(un_elemento))
# print(type(registro))
# print(type("Python"))
# print(type("Python",))

# DESEMPAQUETADO

# dia = 25
# mes = "Septiembre"
# anio = 2026
# fecha = dia, mes, anio
# dia_nac, mes_nac = fecha #Tira error, ya que debe tener misma cantidad de elementos que "Fecha"

# Integración con matrices.
# Una empresa registra las unidades vendidas de tres productos durante cuatro semanas.
# Los códigos de producto se almacenan en una tupla y las cantidades en una matriz
# de 3 x 4, donde cada fila corresponde al producto ubicado en la misma posición
# de la tupla.

# a) Informar el total vendido por producto.
# b) Informar el total de una semana indicada.
# c) Determinar el código del producto con mayor venta acumulada.
# d) Validar la semana ingresada y capturar los errores correspondientes



def TotalPorProducto(matriz):
    ProdTotal = []
    for f in range(len(matriz)):
        ProdTotal.append(sum(matriz[f]))
    return ProdTotal

def TotalPorSemana(matriz):
    SemTotal = []
    for c in range(len(matriz[0])):
        totalcolumna = 0
        for f in range(len(matriz)):
            totalcolumna += matriz[f][c]
        SemTotal.append(totalcolumna)
    return SemTotal


# MAIN
codigos = ("P101", "P205", "P330")
ventas_semanales = [ #FILA = PRODUCTO
 [12, 15, 10, 18],   #COLUMNA = SEMANA
 [8, 11, 9, 14],
 [20, 17, 22, 19]
]

# a) Informar el total vendido por producto.
ProdTotal = TotalPorProducto(ventas_semanales)
print("TOTAL VENDIDO POR PRODUCTO:")
for i in range(len(ProdTotal)):
    print(f"Producto {codigos[i]}: {ProdTotal[i]} unidades")


# b) Informar el total de una semana indicada, y d) Validar la semana ingresada y capturar los errores correspondientes

IngregarSemana = input("Ingrese la semana de la que desea ver el total: ")

if IngregarSemana.isdigit():
    semana = int(IngregarSemana)
    if semana >= 1 and semana <= len(ventas_semanales[0]):
        print(f"El total de productos vendidos de la semana {semana} es de: {TotalPorSemana(ventas_semanales)[semana-1]}")
    else:
        print(f"La semana número {semana}, no existe. Intente nuevamente.")
else:
    print("Valor incorrecto, debe ingresar un número válido.")

# c) Determinar el código del producto con mayor venta acumulada.

cod_mayorventa = codigos[ProdTotal.index(max(ProdTotal))]
print(f"El código de producto con mayor venta acumulada es: {cod_mayorventa}")