producto = input("Producto:")
precio = float(input("Precio unitario:"))
cantidad = int(input("Cantidad:"))
total = precio * cantidad

#A) Usando f-string con formato de dos decimales
print(f"\n a) Con f-string:")
print(f"Producto: {producto} - Precio: ${precio:.2f} - Cantidad: {cantidad} - Total: ${total:.2f}")

#B) Usando concatenacion, convirtiendo explicitamente a str()
print("\n b) Con concatenación:")
print("Producto: " + producto + " - Precio: $" + str(precio) + " - Cantidad: " + str(cantidad) + " - Total: $" + str(total))

