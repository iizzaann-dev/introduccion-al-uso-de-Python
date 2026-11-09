from datos import series

lista = [
    i["titulo"] for i in series if "Drama" in i["generos"]
]

print(lista)