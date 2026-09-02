suma = 0 
cantidad = 0

while True:
    numero = int(input("Ingrese un numero entero (-1 para finalizar):"))
    if numero == -1:
        break
    suma += numero
    cantidad += 1

print("Cantidad de valores ingresados:", cantidad)
print("Suma:", suma)

if cantidad != 0:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
else:
    print("No existen datos para calcular el promedio!")