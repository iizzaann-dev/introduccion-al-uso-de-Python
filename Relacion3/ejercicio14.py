from datos2 import personajes_frieren

for i in personajes_frieren:
    for j in i["afiliacion"]:
        if j == "Asociación Continental de Magia":
            i["afiliacion"].remove("Asociación Continental de Magia")


for k in personajes_frieren:
    print(k, "\n")