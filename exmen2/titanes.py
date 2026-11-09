from datos import personajes

def ejercicio1():
    lista = [
        i["nombre"] for i in personajes if i["afiliacion"] == "Cuerpo de Exploración"
    ]
    print(lista)


def ejercicio2():
    lista = [
        i["nombre"] for i in personajes if i["afiliacion"] == "Cuerpo de Exploración" 
        and "Supervivencia" in i["habilidades"] and "Sigilo" in i["habilidades"]
    ]

    print(lista)

#Muestra una lista de tuplas con el nombre y la afiliación 
#de todos los personajes que no pertenezcan al Cuerpo de Exploración.
def ejercicio3():
    lista = [
        (i["nombre"], i["afiliacion"]) for i in personajes if "Cuerpo de Exploración" not in i["afiliacion"]
    ]
    
    print(lista)
    

#Muestra una lista de cadenas de caracteres que incluya el 
#nombre del personaje seguido de un espacio en blanco y su 
#afiliación entre paréntesis, para todos los personajes que 
#hayan completado 20 misiones o más
def ejercicio4():
    lista = [
        f"{i["nombre"]} {i["afiliacion"]}" for i in personajes 
        if i["registro_combate"]["misiones_completadas"] >= 20
    ]
    
    print(lista)
    

#Muestra una lista de tuplas con los nombres y las alturas en 
#centímetros de todos los personajes que midan más de 1,70 metros.
def ejercicio5():
    lista = [
        (i["nombre"], i["estatura_m"]) for i in personajes if i["estatura_m"] > 1.70
    ]
    
    print(lista)
    

#Muestra una lista aplanada con todas las habilidades de todos los personajes. 
# No importa si hay habilidades repetidas.
def ejercicio6():
    lista = [
        j for i in personajes for j in i["habilidades"]
    ]
    
    print(lista)
    

#Los atributos titanes_solo y titanes_equipo del registro de combate indican 
#la cantidad de titanes que ha matado el personaje en solitario o 
#junto a su equipo, respectivamente. Muestra una lista con los nombres 
#de los personajes que hayan matado 5 o más titanes en total.
def ejercicio7():
    lista = [
        i["nombre"] for i in personajes
        if i["registro_combate"]["titanes_solo"] + i["registro_combate"]["titanes_equipo"] >= 5
    ]
    
    print(lista)
    

#Muestra una lista de diccionarios con los atributos 
#nombre y titanes_totales, donde se muestre el nombre 
#y el número de titanes que ha matado cada personaje en total.

def ejercicio8():
    lista = {
        i["nombre"]: i["registro_combate"]["titanes_solo"] + i["registro_combate"]["titanes_equipo"]
        for i in personajes
    }
    
    print(lista)
    
    

#La función sum nos permite sumar los valores de una lista. 
#Calcula con una comprensión de listas la media de las alturas 
#de todos los personajes y muéstrala.
def ejercicio9():
    altura = 0
    
    lista = [
        sum(i["estatura_m"] for i in personajes)/len(personajes)
    ]
    
    print(lista)
    

#Calcula en una comprensión de listas la media de las alturas de todos los 
#personajes y luego en otra comprensión de listas muestra una lista de tuplas 
#con los nombres y las alturas de los personajes que midan más de la media. 
#Muestra únicamente la lista de tuplas resultante.
def ejercicio10():
    media_alturas = (
        sum([i["estatura_m"] for i in personajes])/len(personajes)
    )
    
    lista = [
        (j["nombre"], j["estatura_m"]) for j in personajes if j["estatura_m"] > media_alturas
    ]
    
    print(lista)
    
ejercicio10()