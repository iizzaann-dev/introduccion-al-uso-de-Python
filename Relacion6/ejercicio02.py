from datos import series

[print(i["titulo"]) for i in series for j in i["generos"] if j == "Fantasía" or j == "Misterio"]

#[print(i["titulo"]) for i in series if "Fantasía" in i["generos"] or "Misterio" in i["generos"]]