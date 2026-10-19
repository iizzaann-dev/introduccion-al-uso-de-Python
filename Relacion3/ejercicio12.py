from datos2 import personajes_frieren

for i in personajes_frieren:
    if i["raza"] == "Demonio":
        personajes_frieren.remove(i)

for i in personajes_frieren:
    print(i, "\n")