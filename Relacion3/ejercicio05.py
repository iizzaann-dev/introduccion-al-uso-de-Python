from datos import pokemons

for i in pokemons:

    for j in i["tipos"]: 
        if j.endswith("a"):
            print(f"El pokemon {i["nombre"]} es de un tipo que acaba en a.")
            break

    """
    for i in pokemons:
        for j in i["tipos"]:
            if j[-1] == "a":
                break
    """

    