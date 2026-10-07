from datos import pokemons

max = 0
pokemonSingular = []


for i in pokemons:

    if i["peso_kg"] > max:
        max = i["peso_kg"]

        pokemonSingular = i


print(f"El pokemon más pesado es {pokemonSingular["nombre"]} y pesa: {pokemonSingular["peso_kg"]}")