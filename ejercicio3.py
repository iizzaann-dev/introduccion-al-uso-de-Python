edad = int(input("Ingresa la edad de una persona: "))

if edad < 0:
    print(f"La edad {edad} no es posible.") 

elif edad >= 120: 
    print(f"La edad {edad} es propia de un vampiro.") 

else:

    if edad < 18:
        print(f"Tu edad es {edad}, por lo que eres menor de edad.") 

    else:
        print(f"Tu edad es {edad}, por lo que eres mayor de edad.") 
