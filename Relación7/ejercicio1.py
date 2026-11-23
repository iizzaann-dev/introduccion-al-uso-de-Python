def comprobarLetraDNI(DNI: str) -> bool:
    letras_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"

    DNI = DNI.upper().strip()
    
    #DNI[:-1].isdigit() comprueba si todos los caracteres menos el último son numeros
    #DNI[-1].isalpha() comprueba si el último caracter es una letra
    if len(DNI) == 9 and DNI[:-1].isdigit() and DNI[-1].isalpha():
        numeros = int(DNI[:-1]) #Convierte a int todos los numeros de la cadena de texto menos el ultimo caracter
        letra = letras_DNI[numeros % 23] #Calcula la letra del dni y selecciona la letra con el resto que de al hacer %23
        return DNI[-1] == letra #Devuelve True si la letra del dni concuerda con la calculada que deberia ser
    
    else:
        return False
    
if comprobarLetraDNI("12345678z") == True:
    print("El DNI es correcto.")
    
else:
    print("El DNI no es correcto.")

    
    