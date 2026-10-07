#Pedir al usuario dos números enteros (base y exponente). Calcular el resultado de
#elevar la base al exponente. Mostrar un error en caso de que la base sea menor que
#1 o que la exponente sea menor que 0.

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa la potenia: "))
potencia = 0

if base < 1:
    print("Error. La base es menor que 1.") 

elif exponente < 0: 
    print("Error. La exponente es menor que 0.")

else:
    potencia = base ** exponente    

print(f"La potencia de {base} (base) y {exponente} (exponente) es {potencia}.") 
