def calcular_importe(cantidad, precio):
    importe = cantidad * precio
    assert importe > 0
    return importe


productos = []

while True:
    codigo = input("Ingrese código del producto (FIN para terminar): ")
    if codigo == "FIN":
        break

    descripcion = input("Ingrese descripción: ")

    try:
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese precio: "))

        if cantidad <= 0 or precio <= 0:
            raise ValueError("La cantidad y el precio deben ser mayores a cero")

        importe = calcular_importe(cantidad, precio)
        productos.append((codigo, descripcion, cantidad, precio, importe))

    except ValueError as mensaje:
        print("Producto no incorporado:", mensaje)

#Programa Principal
cantidad_productos = len(productos)
importe_total = 0

for producto in productos:
    importe_total = importe_total + producto[4]

print("Cantidad de productos cargados:", cantidad_productos)
print("Importe total:", importe_total)

if cantidad_productos != 0:
    precio_promedio = importe_total / cantidad_productos
    print(f"Precio promedio: {precio_promedio:.2f}")
else:
    print("No se cargaron productos, no se puede calcular el promedio")