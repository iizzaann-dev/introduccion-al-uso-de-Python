from datos import jugadores


[print(i["nombre"], "\n") for i in jugadores if i["dorsal"] == 10]