from datos2 import personajes_frieren

for i in personajes_frieren:
    if i["raza"] == "Elfo":
        i["afiliacion"].append("Elfos Supervivientes del Examen de Python")

for j in personajes_frieren:
    print(j, "\n")