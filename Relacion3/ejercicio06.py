from datos import pokemons

lista = {
    "nombre": "Arcanine",
    "generacion": 1,
    "categoria": "Legendario",
    "tipos": ["Fuego"],
    "peso_kg": 155.0,
    "altura_m": 1.9
}

pokemons.append(lista)


print(f"El nuevo pokemon es: {pokemons[-1]}") 