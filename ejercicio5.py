num1 = int(input("Ingresa el valor del primer número: "))
num2 = int(input("Ingresa el valor del segundo número: "))
acumulador = 0

if num1 > num2:
    print("Error")

else:

    for i in range(num1, (num2 + 1)):
        if i % 2 == 0:
            print(f"El número {i} es par.") 

        else:
            print(f"El número {i} es impar.") 


    while acumulador <= num2:

        if acumulador % 2 == 0:
            print(f"El numero {acumulador} es par.") 

        else:
            print(f"El número {acumulador} es impar.")

        acumulador += 1



