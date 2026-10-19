from peliculas import peliculas

peliculas_infantiles = []

for i in peliculas:
    if i["edad_recomendada"] == 0:
        i["generos"].append("Infantil")

for i in peliculas:
    if "Infantil" in i["generos"]:
        peliculas_infantiles.append(i)

for k in peliculas_infantiles:
    print(k, "\n")