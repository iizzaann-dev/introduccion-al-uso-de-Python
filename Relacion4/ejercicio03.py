from peliculas import peliculas

for i in peliculas:
    for j in i["generos"]:
        if j == "Drama":
            i["edad_recomendada"] = 18

for k in peliculas:
    print(k, "\n")


