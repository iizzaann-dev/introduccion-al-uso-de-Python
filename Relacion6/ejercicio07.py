from datos import series

lista = [
    (i["titulo"], j["comentario"]) for i in series for j in i["reseñas"] if j["nota"] == 10
]

print(lista)