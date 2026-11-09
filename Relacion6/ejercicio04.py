from datos import series

lista = [
    (i["titulo"], j["nota"]) for i in series for j in i["reseñas"] if j["usuario"] == "Elena"
]

print(lista)