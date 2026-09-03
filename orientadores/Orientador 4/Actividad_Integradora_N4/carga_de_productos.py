'''Desarrollen un programa modular que permita cargar productos. Cada producto se representará mediante una tupla 
(codigo, descripcion, precio) y todos los productos se almacenarán en una lista. 
La carga finalizará cuando el código sea  "FIN".


Implementen las siguientes funciones:
• cargar_productos(): retorna la lista de tuplas cargadas.
• mostrar_productos(productos): muestra el catálogo.
• buscar_producto(productos, codigo): retorna la tupla encontrada o None.
• producto_mayor_precio(productos): retorna la tupla de mayor precio o None si la lista está vacía.
• precio_promedio(productos): retorna el promedio o None si no existen productos.
Durante la carga:
• No incorporen códigos repetidos.
• No intenten modificar una tupla existente. Para actualizar un precio, reemplacen en la lista el registro completo por una 
nueva tupla'''


import funciones

productos = funciones.cargar_productos()

funciones.mostrar_productos(productos)

if productos:
    codigo = input("Ingresar codigo a buscar: ")
    buscado = funciones.buscar_producto(productos, codigo)

    if buscado is None: 
        print('El producto buscado no existe')
    else:
            print(f'El producto buscado esta disponible:')
            print(f'Codigo: {buscado[0]}\nDescripción: {buscado[1]}\nPrecio: {buscado[2]}\n')


if not productos:
      print("No se han cargado productos")
else:
    mayor = funciones.producto_mayor_precio(productos)
    promedio = funciones.precio_promedio(productos)
    print(f'El producto de mayor precio es:')
    print(f'Codigo: {mayor[0]}\nDescripción: {mayor[1]}\nPrecio: {mayor[2]}\n')

    print(f'El promedio es de {promedio}')

if productos:
    modificacion = input("Queres realizar una modificación de precio? (si/no)")

    if modificacion.lower() == 'si':
        actualizacion = funciones.actualizar_precio(productos)
        if actualizacion:
                print("Se ha modificado correctamente")
                print("El nuevo catalogo quedaría de la siguiente forma: ")
                funciones.mostrar_productos(productos)
        else:
            print("No se pudo actualizar: el código no existe")

