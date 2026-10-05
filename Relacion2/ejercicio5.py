#Pedir al usuario un número y mostrar el triángulo de pascal de ese número de listas.
#En caso de que el número sea inferior a 1, mostrar un mensaje de error.

numero = int(input("Ingresa un número superior a 1: "))

lista = [1]
lista2 = []

if numero < 1:
    print("El número introducido es menor a 1.")

else:
    for i in range (numero):

        print(" " * (numero - i), lista)

        lista2 = [1]
        for j in range(len(lista) - 1):
            a = lista[j]
            b = lista[j + 1]

            lista2.append(a + b)

        lista2.append(1)
        lista = lista2



