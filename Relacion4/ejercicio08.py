from peliculas import peliculas

for i in peliculas:
    if i["edad_recomendada"] == 0:
        peliculas.remove(i)


for j in peliculas:
    print(j, "\n")