# numero = int(input("Ingrese un número: "))
# resultado = 100 / numero
# print(resultado)

# Preventivo
# numero = input("Ingrese un número: ")
# if numero !=0 and numero != "0" and numero.isdigit():
#     resultado = 100 / int(numero)
#     print(resultado)
# else:
#     print("El número ingresado no es válido.")

# Correctivo

lista = []
while True:
    try:
        numero = int(input("Ingrese un número: "))
        resultado = 100 / numero
        lista.append(resultado)
        print(lista)
    except (ZeroDivisionError, ValueError):
        print("El número ingresado no es válido")
    