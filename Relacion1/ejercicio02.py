precio = float(input("Ingresa el precio del producto: "))
iva = input("Ingresa el tipo de IVA (General, Reducido, Superreducido): ") 

if iva.lower() == "general":
    precioFinal = precio * 1.21
    print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}") 

elif iva.lower() == "reducido":
    precioFinal = precio * 1.10
    print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}") 


elif iva.lower() == "superreducido":
    precioFinal = precio * 1.04
    print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}") 

else:
    print(f"El tipo de iva {iva} no existe.")

match iva.lower(): 
    case "general":
        precioFinal = precio * 1.21
        print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}") 

    case "reducido":
        precioFinal = precio * 1.10
        print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}")

    case "superreducido":
        precioFinal = precio * 1.04
        print(f"El precio del producto ingresa con el iva {iva} aplicado es {precioFinal}")

    case _:
        print("Error")