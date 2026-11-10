from datos import lista

def ejercicio1():
    Fuerza = {       
        "nombre": "Pablo",
        "raza": "Humano",
        "ocupacion": "Investigador",
        "estilo_combate": ["lento", "profundo"],
        "atributos": {"fuerza": 60, "defensa": 80, "velocidad": 80}
    },

    lista.append(Fuerza)

#Hay una coma despues de la lista pero está entero bien el ejercicio

def ejercicio2():
    fuerza = 0
    defensa = 0
    velocidad = 0
    mediaFuerza = 0

    for i in lista:
        fuerza = i["atributos"]["fuerza"]
        defensa = i["atributos"]["defensa"]
        velocidad = i["atributos"]["velocidad"]

        mediaFuerza = (fuerza + defensa + velocidad) / 3

    if mediaFuerza > 85:
        print(i)


#Mal porque se reinicia la media


def ejercicio3():
    fuerza = 0
    acumulador = 0
    mediaFuerza = 0

    for i in lista:
        fuerza = i["atributos"]["fuerza"]
        acumulador += fuerza

    mediaFuerza = acumulador / len(lista)

    for j in lista:
        if j["atributos"]["fuerza"] > mediaFuerza:
            print(j)

#Está correcrto

def ejercicio4():
    for i in lista:
        for j in i["estilo_combate"]:
            if j == "Respiración del Agua":
                if (i["atributos"]["defensa"] + 10) <= 100:
                    i["atributos"]["defensa"] += 10

    for k in lista:
        print(f"{k["nombre"]} {k["atributos"]["defensa"]}") 
        
#Si llega a los 100 no se suma nada

def ejercicio5():
    numero4 = 0

    for i in lista:
        if i["atributos"]["defensa"] < "Zenitsu Agatsuma"["atributos"]["fuerza"]:
            print(f"{i["nombre"]} {i["atributos"]["fuerza"]} {i["atributos"]["defensa"]}")
            
#Totalmente mal


def ejercicio6():
    for i in lista:
        if i["ocupacion"] == "Cazador de demonios":
            lista.remove(i)

    print(lista)
    
#No hace la copia de la lista pero quitando eso esta bien toda la estructura
