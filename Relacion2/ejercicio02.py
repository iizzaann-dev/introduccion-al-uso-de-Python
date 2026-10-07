#Pedir al usuario un número entero y calcular el factorial desde 1 hasta dicho número
#(incluido). Si el número introducido es menor que 1, mostrar un mensaje de error.

numero = int(input("Ingresa un número entero mayor que 1: "))

factorial = 1

if numero < 1: 
    print("El número introducido es menor que 1.")

else:
    for i in range(1, numero + 1):
        factorial *= i

print(f"El factorial del número {numero} es: {factorial}") 