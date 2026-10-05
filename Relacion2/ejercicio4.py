#Pedir al usuario un número entero y añadir todos los números de la serie de
#fibonacci desde 0 hasta ese número (incluido) a una lista. Mostrar dicha lista al
#acabar. Si el número introducido es menor que 0, mostrar un mensaje de error.

numero = int(input("Ingresa un número entero: "))

suma = 0

lista = []

if  numero < 0:
    print("Error. El número es menor que 0.")

else:

    a = 0
    b = 1

    for i in range (numero + 1):

        if a > numero:
            break

        lista.append(a)

        c = a + b
        a = b
        b = c


print(lista)
