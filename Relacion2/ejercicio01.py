#Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
#número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
#error.

numero  = int(input("Ingresa un número superior a uno: "))
suma = 0

if numero > 1: 
    for i in range (1, numero + 1):
        suma += i
else:
    print("El número introducido es menor a 1.")

print(f"El sumatorio de todos los numeros del 1 al {numero} es {suma}.") 