'''Desarrollen un programa que solicite dos números y calcule su división. Utilicen:
except ValueError para datos no numéricos.
except ZeroDivisionError para un divisor igual a cero.
else para mostrar el resultado solamente si el bloque try finalizó sin excepciones.
finally para mostrar un mensaje de cierre que se ejecute exista o no un error.
'''



try:
    num1 = int(input("Solicitar primer número: "))
    num2 = int(input("Solicitar segundo número: "))
    resultado = num1/num2

except ValueError:
    print("Error. Ingresar solo datos númericos")
except ZeroDivisionError:
    print("Error. No se puede dividir por 0, ingresar otro número.")
else:
    print(f"El resultado de la división es {resultado}")
finally:
    print("El programa ha finalizado")



