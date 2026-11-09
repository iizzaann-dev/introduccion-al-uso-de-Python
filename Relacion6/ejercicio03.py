from datos import series

[print(i["titulo"]) for i in series if i["nota"] >= 9 and len(i["generos"]) >= 3]