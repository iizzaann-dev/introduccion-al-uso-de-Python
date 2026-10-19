from peliculas import peliculas

for i in peliculas:
    if i["edad_recomendada"] == 0:
        i["generos"].append("Infantil")

for j in peliculas:
    print(f"{j["titulo"]}: {j["generos"]}", {j["edad_recomendada"]})
