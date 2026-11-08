from datos import jugadores

[print(i["nombre"]) for i in jugadores if 9 in [i["atributos"][j] for j in i["atributos"]]]