from datos import pokemons

altura = 0
acumulador = 0

for i in pokemons:
    altura = i["altura_m"] + altura
    acumulador += 1

resultado = altura /acumulador 

lista = []

for i in pokemons:
    if i["altura_m"] < resultado:
        lista.append(i)


print("Los pokemons que tienen menos altura que la media son: ") 

for i in lista:
    print(f"{i["nombre"]}: {i["altura_m"]}") 