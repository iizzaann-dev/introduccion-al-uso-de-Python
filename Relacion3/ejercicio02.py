#Mostrar la media de altura de todos los pokemons

from datos import pokemons

altura = 0
acumulador = 0

for i in pokemons:
    altura = i["altura_m"] + altura
    acumulador += 1

resultado = altura /acumulador 

print(f"La media de altura de todos los pokemons es: {resultado:.2f} m.")
