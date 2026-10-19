from datos import pokemons

for i in pokemons:
    if "Agua" in i["tipos"]:
        print(f"El pokemon {i["nombre"]} es tipo agua.") 
