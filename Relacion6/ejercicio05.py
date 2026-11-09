from datos import series

[print(j["comentario"], "\n") for i in series for j in i["reseñas"] if len(j["comentario"].replace(" ", "").replace("\n", "").replace("\t", "")) > 40]