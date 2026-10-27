"""
Desarrollar una función crear_alumnos() que genere alumnos.txt. Por cada alumno se ingresarán legajo, nombre y  apellido, y comisión.
La carga finalizará con un legajo igual a -1; ese valor de corte no debe grabarse. Cada registro deberá almacenarse en una línea con
sus campos separados por punto y coma. Antes de escribir, validen  que el legajo sea positivo, que el nombre no esté vacío y que la
comisión tenga un formato válido (valor numérico de 1 a  10).

Prueben la función con varios alumnos. Luego ejecútenla nuevamente usando modo "wt" y expliquen qué ocurrió con los datos anteriores.
Repitan con modo "at" y comparen los resultados.

"""
def crear_alumnos():
    try:
        archivo = open(r"alumnos.txt", "at")
    except OSError:
        print("No se pudo crear el archivo.")
    else:
        legajo = int(input("Ingrese su número de legajo (-1 para finalizar): "))
        while legajo != -1:
            if legajo < 1:
                print("El legajo debe ser positivo. Intente nuevamente.")
            else:
                nombre = input("Ingrese su nombre: ")
                while nombre.isspace() or nombre == "":
                    print("El nombre no puede estar vacío. Intente nuevamente.")
                    nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                while apellido.isspace() or apellido == "":
                    print("El apellido no puede estar vacío. Intente nuevamente.")
                    apellido = input("Ingrese su apellido: ")
                comision = int(input("Ingrese su comisión: "))
                while comision > 10 or comision < 1:
                    print("La comisión ingresada no esta dentro del formato valido (1 a 10). Intente nuevamente.")
                    comision = int(input("Ingrese su comisión: "))
                archivo.write(f"{str(legajo)}; {nombre}; {apellido}; {str(comision)}\n")
            legajo = int(input("Ingrese su número de legajo: "))
        archivo.close()
        
def mostrar_alumnos():
    try:
        archivo = open(r"alumnos.txt", "rt")
    except OSError:
        print("Error, no se pudo abrir el archivo.")
    else:
        linea = archivo.readline()
        print("Todos los registros válidos:")
        contador_comisiones = {}
        contador = 0
        while linea:
            campos = linea.rstrip("\n").split("; ")
            if len(campos) == 4:
                legajo, nombre, apellido, comision = campos
                try:
                    legajo = int(legajo)
                    comision = int(comision)
                except ValueError:
                    contador += 1  
                else:      
                    if comision in contador_comisiones:
                        contador_comisiones[comision] += 1
                    else:
                        contador_comisiones[comision] = 1

                    print(f"Legajo: {legajo}, nombre: {nombre}, apellido: {apellido}, comisión: {comision}")
                    if legajo > 10000:
                        print("Posee legajo mayor a 10000.\n")
            else:
                contador += 1           
            linea = archivo.readline()
        archivo.close()    

        print("Las lineas que no respetan el formato esperado son: ", contador, "\n")
        print("Contador de alumnos en cada comisión: ")
        for comision, cantidad in contador_comisiones.items():
            print(f"Comisión: {comision}, cantidad: {cantidad}")

mostrar_alumnos()