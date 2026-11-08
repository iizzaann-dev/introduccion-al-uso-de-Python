from datos import jugadores

lista = [j for i in jugadores for j in i["filigranas"]]

print(lista)