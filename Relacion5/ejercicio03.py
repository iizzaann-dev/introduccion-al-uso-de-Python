from datos import jugadores

[print(i["nombre"]) for i in jugadores if i["equipo"] == "FC Barcelona"]