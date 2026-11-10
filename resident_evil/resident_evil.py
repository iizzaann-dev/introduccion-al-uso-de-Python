from datos import personajes

def ejercicio1():
    lista = [
        i["nombre"] for i in personajes if i["vivo"] == True 
        and i["afiliacion"] == "Policía de Raccoon City"
    ]

    print(lista)


def ejercicio2():
    lista = [
        i["nombre"] for i in personajes if i["afiliacion"] == "Policía de Raccoon City" 
        and "Pistola Samurai Edge" in i["armas"] and "Lanzagrandas" in i["armas"]
    ]

    print(lista)


def ejercicio3():
    lista = [
        (i["nombre"], i["afiliacion"]) for i in personajes 
        if i["afiliacion"] != "Policía de Raccoon City"
    ]

    print(lista)


def ejercicio4():
    lista = [
        f"{i['nombre']} ({i['afiliacion']})" for i in personajes 
        if i["registro_zombies"]["misiones_completadas"] >= 20
    ]

    print(lista)


def ejercicio5():
    lista = [
        (i["nombre"], i["estatura_m"] * 100) for i in personajes if i["estatura_m"] > 1.70
    ]

    print(lista)


def ejercicio6():
    resultado = []
    lista = [
        j for i in personajes for j in i["armas"]
    ]

    print(lista)

def ejercicio7():
    lista = [
        i["nombre"] for i in personajes
        if i["registro_zombies"]["zombies_solo"] + i["registro_zombies"]["zombies_equipo"] >= 100
    ]

    print(lista)


def ejercicio8():
    lista = {
        i["nombre"]: i["registro_zombies"]["zombies_solo"] + i["registro_zombies"]["zombies_equipo"] for i in personajes
    }

    print(lista)


def ejercicio9():
    lista = [
        sum(i["estatura_m"] for i in personajes) / len(personajes)
    ]

    print(lista)


def ejercicio10():
    lista = sum([
        i["estatura_m"] for i in personajes ]) / len(personajes)

    alturas = [
        (i["nombre"], i["estatura_m"]) for i in personajes if i["estatura_m"] >= lista
    ]

    print(alturas)



