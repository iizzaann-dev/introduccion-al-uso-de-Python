cantidad = float(input("Ingresa la cantidad de lluvia que ha caido en las últimas 12 horas: "))

if cantidad < 60:
    print(f"La cantidad de lluvia ({cantidad}) es menor a 60, por lo que NO HAY ALERTA.") 

elif cantidad in [60, 119]:
    print(f"La cantidad de lluvia ({cantidad}) está entre los 60mm y los 120mm por lo que HAY ALERTA AMARILLA.") 

elif cantidad >= 120:
    print(f"La cantidad de lluvia ({cantidad}) es igual o superior a los 120mm por lo que HAY ALERTA ROJA.")

elif cantidad <= 0:
    print(f"La cantidad introducida ({cantidad}) no es válida.") 

match cantidad:

    case n if n <= 60:
        print(f"La cantidad de lluvia ({cantidad}) es menor a 60, por lo que NO HAY ALERTA.") 

    case n if n in range(60, 120):
        print(f"La cantidad de lluvia ({cantidad}) está entre los 60mm y los 120mm por lo que HAY ALERTA AMARILLA.") 

    case n if n >= 120:
        print(f"La cantidad de lluvia ({cantidad}) es igual o superior a los 120mm por lo que HAY ALERTA ROJA.") 

    case _:
        print("Error")

