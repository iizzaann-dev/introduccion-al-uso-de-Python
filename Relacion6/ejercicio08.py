from datos import series

lista = [
    (i["titulo"], "Obra maestra" if sum(j["nota"] for j in i["reseñas"])/len(i["reseñas"]) >= 9 else "Gran serie") for i in series
]


print(lista)