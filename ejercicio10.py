num1 = int(input("Ingresa el valor del primer número: "))
num2 = int(input("Ingresa el valor del segundo número: "))


if num1 > num2: 
    print(f"Error, el primer número es mayor que el segundo. {num1} > {num2}") 

else:
    for i in range(num1, (num2 + 1)):

        es_primo = True

        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break

        if es_primo:
            print(f"El numero {i} es primo.")

        else:
            print(f"El número {i} no es primo.") 
        