def cargar_productos():
    productos = []
    codigo = input("Ingresar código (FIN para terminar): ")
    while codigo.upper() != "FIN": #Normalización para finalizar carga
        if buscar_producto(productos, codigo) is not None: #Validacion de codigo repetido
            print("Error: el código ya existe.")
            codigo = input("Ingresar código (FIN para terminar): ")
        else:
            descripcion = input("Ingresar descripción: ")
            precio = float(input("Ingresar precio: "))
            producto = (codigo, descripcion, precio)
            productos.append(producto)
            codigo = input("Ingresar código (FIN para terminar): ")
    return productos

def mostrar_productos(productos):
    for i in range(len(productos)):
        print(f'{i+1} producto:')
        print(f'Codigo: {productos[i][0]}\nDescripción: {productos[i][1]}\nPrecio: {productos[i][2]}\n')

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto[0].upper() == codigo.upper(): #Evitamos problemas de ingreso de datos con upper()
            return producto
    return None

def precio_promedio(productos):
    if not productos:
        return None

    suma = 0
    for precio in productos:
        suma += precio[2]
    promedio = suma/len(productos)
    return promedio

def producto_mayor_precio(productos):
    if not productos:
        return None

    mayor = productos[0]
    for producto in productos:
        if producto[2] > mayor[2]:
            mayor = producto
    return mayor


def actualizar_precio(productos):
    codigo = input("Ingresar código del producto a reemplazar precio: ")
    precio_nuevo = float(input("Ingresar precio nuevo: "))

    for i in range(len(productos)):
        if productos[i][0].upper() == codigo.upper():
            productos[i] = (productos[i][0], productos[i][1], precio_nuevo) # Volvemos a armar la tupla en vez de cambiarla
            print("Precio actualizado.")
            return True

    print("Código no encontrado.")
    return False

            
