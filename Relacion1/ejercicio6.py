contrasena = input("Ingresa la contraseña: ") 

condicion = False


while condicion == False:

    if contrasena != "12345":
        print(f"La contraseña {contrasena} no es correcta, intentelo de nuevo.") 
        contrasena = input("Ingresa la contraseña: ") 


    else:
        print(f"La contraseña introducida es correcta.")
        condicion = True