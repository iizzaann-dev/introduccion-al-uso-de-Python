from datos import jugadores

[print(i["nombre"]) for i in jugadores if len(i["filigranas"]) > 2]