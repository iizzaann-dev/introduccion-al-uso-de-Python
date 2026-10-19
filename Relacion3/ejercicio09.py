from datos2 import personajes_frieren

for i in personajes_frieren:
    for j in i["afiliacion"]:
        if j == "Magos de Primera Clase":
            print(f"{i["nombre"]} es un/a {i["raza"]}/a y es un Mago/a de primera clase.") 
            break