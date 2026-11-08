from datos import jugadores

[print(i["nombre"]) for i in jugadores if i["atributos"]["tiro"] >= 8 and i["atributos"]["regate"] >= 9]