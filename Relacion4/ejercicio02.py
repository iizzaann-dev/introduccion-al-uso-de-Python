from peliculas import peliculas

duracion = 0

for i in peliculas:
    duracion += i["duracion"] 

media = duracion / len(peliculas)
print(f"La media es {media} mins. \n") 

for j in peliculas: 
    if j["duracion"] > media:
        print(f"{j["titulo"]}: {j["duracion"]} mins") 