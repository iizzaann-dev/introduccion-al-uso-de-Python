from datos2 import personajes_frieren

for i in personajes_frieren:
    for j in i["afiliacion"]:
        if j == "Grupo de los Cuatro Héroes":
            print(f"Nombre: {i["nombre"]}, Raza: {i["raza"]}, Edad: {i["edad"]}") 
