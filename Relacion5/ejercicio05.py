from datos import jugadores

[print(i["nombre"]) for i in jugadores if "ruleta" in i["filigranas"]]