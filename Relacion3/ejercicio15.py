from datos2 import personajes_frieren

for i in personajes_frieren:
    if i["raza"] == "Humano" and i["edad"] >= 100:
        i["raza"] = "Zombie"
        print(i) 
        break



