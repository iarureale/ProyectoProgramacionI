'''Desarrollar un programa para gestionar las entregas del Proyecto Integrador mediante entregas.csv. 
Cada registro  contendrá número de grupo, nombre del proyecto, integrante responsable y porcentaje de avance.

Dividan la solución en funciones para:
    Crear el archivo y escribir una única fila de encabezado.
    Cargar entregas sin repetir el número de grupo.
    Mostrar todas las entregas válidas.
    Buscar una entrega por número de grupo.
    Informar los proyectos con avance inferior al 50 %.
    Calcular el promedio de avance sin dividir por cero cuando no haya registros válidos.
    Informar y omitir registros mal formados sin interrumpir todo el procesamiento.

Validen que el número de grupo sea positivo, que los campos de texto no estén vacíos y que 
el porcentaje se encuentre entre 0 y 100. Procesen el archivo una sola vez por operación y eviten 
cargarlo completo en memoria cuando no sea necesario
'''

def crear_archivo():
    try:
        arch = open(r"entregas.csv", mode="wt")
    except OSError:
        print("El archivo no ha podido ser creado")
    else:
        arch.write("numero_grupo;nombre_proyecto;integrante_responsable;porcentaje_avance\n")
        arch.close()
        print("Archivo creado con su encabezado")

def pedir_grupo():
    while True:
        try:
            grupo = int(input("Ingresar número de grupo: "))
            return grupo
        except ValueError:
            print("Solo se puede ingresar número de grupo")

def validar_repitencia(grupo):
    unico = True
    try:
        arch = open("entregas.csv", mode = 'rt')
    except OSError:
        print("No se pudo abrir el archivo.")
        unico = False
    else:
        for linea in arch:
            if linea.split(';')[0] == str(grupo):
                print("El grupo ingresado no es valido. Ya se encuentra en el archivo")
                unico = False
                break
        arch.close()
    return unico

def validar_grupo(grupo):
    while grupo != -1 and (grupo <= 0 or not validar_repitencia(grupo)):
        if grupo <= 0:
            print("El grupo debe ser positivo.")
            grupo =pedir_grupo()
        else:
            print("El grupo debe ser único")
            grupo = pedir_grupo()
    return grupo


def validar_nombre(nombre):
    while nombre.strip() == '' or ';' in nombre:
        print("El campo ingresado no puede estar vacío ni contener ';'.")
        nombre = input("Ingresarlo nuevamente: ")
    return nombre.strip()

def cargar_porcentaje():
    while True:
        try:
            porcentaje = float(input("Ingresar porcentaje de progreso del proyecto: "))
            while porcentaje < 0 or porcentaje > 100:
                print("Ingresar un porcentaje valido entre 0 y 100.")
                porcentaje = float(input("Ingresar porcentaje de progreso del proyecto: "))
            return porcentaje
        except ValueError:
            print("Solo se permiten números.")

def cargar_entregas():
    grupo = pedir_grupo()
    while grupo != -1:
        print("Ingresar -1 como grupo para finalizar.")
        grupo = validar_grupo(grupo)

        proyecto = input("Nombre del proyecto: ")
        proyecto = validar_nombre(proyecto)

        integrante = input("Integrante responsable: ")
        integrante = validar_nombre(integrante)
        porcentaje = cargar_porcentaje()

        try:
            arch = open("entregas.csv", mode='at')
        except OSError:
            print("El archivo no se pudo abrir")
        else:
            arch.write(str(grupo) + ';' + proyecto + ';' + integrante + ';' + str(porcentaje) +"\n")
            arch.close()
        grupo = pedir_grupo()


def validar_registro(linea):
    valido = True
    campos = linea.strip().split(';')
    if len(campos) != 4:
        print("Registro omitido (cantidad de campos incorrecta):", linea.strip())
        valido = False
    else:
        try:
            grupo = int(campos[0])
            porcentaje = float(campos[3])
        except ValueError:
            print("Registro omitido (grupo o porcentaje no numérico):", linea.strip())
            valido = False
        else:
            if grupo <= 0:
                print("Registro omitido (grupo no positivo):", linea.strip())
                valido = False
            elif campos[1].strip() == '' or campos[2].strip() == '':
                print("Registro omitido (campo de texto vacío):", linea.strip())
                valido = False
            elif porcentaje < 0 or porcentaje > 100:
                print("Registro omitido (porcentaje fuera de rango):", linea.strip())
                valido = False
    return valido


def mostrar_entregas():
    try:
        arch = open("entregas.csv", mode='rt')
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()
        for linea in arch:
            if validar_registro(linea):
                grupo, proyecto, integrante, porcentaje = linea.strip().split(';')
                print("Grupo:", grupo, "| Proyecto:", proyecto,
                      "| Responsable:", integrante, "| Avance:", porcentaje, "%")
        arch.close()


def buscar_entrega():
    print("Ingresar codigo a buscar.")
    buscado = pedir_grupo()
    try:
        arch = open("entregas.csv", mode='rt')
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        encontrado = False
        arch.readline()
        for linea in arch:
            if linea.split(';')[0] == str(buscado):
                if validar_registro(linea):
                    grupo, proyecto, integrante, porcentaje = linea.strip().split(';')
                    print("Grupo:", grupo, "| Proyecto:", proyecto,
                          "| Responsable:", integrante, "| Avance:", porcentaje, "%")
                    encontrado = True
                break
        arch.close()
        if not encontrado:
            print("No se encontró una entrega válida para el grupo", buscado)

def informe_proyectos():
    try:
        arch = open("entregas.csv", mode='rt')
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        inferiores = False
        arch.readline()
        for linea in arch:
            if validar_registro(linea):
                grupo, proyecto, integrante, porcentaje = linea.strip().split(';')
                if float(porcentaje) < 50:
                    print("Grupo:", grupo, "| Proyecto:", proyecto,
                          "| Responsable:", integrante, "| Avance:", porcentaje, "%")
                    inferiores = True
        arch.close()
        if not inferiores:
            print("No hay proyectos con avance inferior al 50 %.")


def calcular_promedio():
    acom = 0
    cont = 0
    try:
        arch = open("entregas.csv", mode='rt')
    except OSError:
        print("No se pudo abrir el archivo.")
    else:
        arch.readline()
        for linea in arch:
            if validar_registro(linea):
                porcentaje = float(linea.strip().split(';')[3])
                acom += porcentaje
                cont += 1
        arch.close()
        if cont == 0:
            print("No hay registros validos para realizar un promedio.")
        else:
            promedio = acom/cont
            print("El promedio de desarrollo es:", promedio)


def main():
    crear_archivo()
    cargar_entregas()
    mostrar_entregas()
    buscar_entrega()
    informe_proyectos()
    calcular_promedio()


main()