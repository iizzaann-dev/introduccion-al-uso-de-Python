from datos import jugadores

lista = [(i["nombre"], "Goleador" if i["atributos"]["tiro"] >= 9 else "Asistente") for i in jugadores]

print(lista)