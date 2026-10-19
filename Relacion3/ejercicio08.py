from datos2 import personajes_frieren

edades, contador = 0, 0

for i in personajes_frieren:
    if i["raza"] == "Humano":
        edades += i["edad"]
        contador += 1

media = edades / contador

print(f"La media de edades de los personajes humanos es: {media}") 

