from peliculas import peliculas

for i in peliculas:
    if i["edad_recomendada"] >=7 and i["edad_recomendada"] <= 13:
        print(f"{i["titulo"]}: {i["edad_recomendada"]}") 