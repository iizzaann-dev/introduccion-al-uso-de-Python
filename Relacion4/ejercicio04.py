from peliculas import peliculas

for i in peliculas:
    if "Fantasía" in i["generos"] and "Aventura" in i["generos"]:
        print(f"{i["titulo"]}: {i["generos"]}") 