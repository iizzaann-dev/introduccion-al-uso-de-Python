from datos import pokemons

"""copia de la lista pokemons"""
for i in pokemons[:]:
    for j in i["tipos"]:
        if j == "Normal":
            pokemons.remove(i)
            break

for i in pokemons:
    print(i["nombre"], i["tipos"]) 
