def ingresar_equipo(equipo, roles):
    cantidad = int(input("Ingresar cantidad de miembros (Maximo 4): "))
    while cantidad < 1 or cantidad > 4:
        print("Dato invalido, ingresar una cantidad permitida")
        cantidad = int(input("Ingresar cantidad de miembros (Maximo 4): "))
    for i in range (cantidad):
        miembro = input(f"Ingresar nombre del miembro{i+1}: ")
        rol = input(f"Ingresar rol del miembro{i+1}: ")
        equipo.append(miembro)
        roles.append(rol)

def mostrar(equipos, roles, nombre_equipo, comision):
    for i in range(len(equipos)):
        print(f"Nombre del miembro {i+1}: {equipos[i].title()}, su rol es {roles[i]}")
    print(f"El nombre del equipo es {nombre_equipo.upper()}, contiene {len(nombre_equipo)} caracteres")
    print(f"El equipo es parte de la comisión {comision}")

def inicial(nombre_equipo):
    formacion = nombre_equipo.split()
    sigla = ""
    for palabra in formacion:
        sigla += palabra[0].upper()
    return sigla

def verificacion(nombre_equipo):
    tiene_digito = False

    for caracter in nombre_equipo:
        if caracter.isdigit():
            tiene_digito = True

    if tiene_digito is not True:
        print(f"El nombre {nombre_equipo.upper()} no contiene digitos")
    else:
        print(f"El nombre {nombre_equipo.upper()} contiene digitos")


