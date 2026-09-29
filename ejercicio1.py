nota = int(input("Ingresa tu nota: "))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print(f"Tu nota es {nota}, por lo que estas suspenso.")

    case 5 | 6:
        print(f"Tu nota es {nota}, por lo que tienes un bien.")

    case 7 | 8:
        print(f"Tu nota es {nota}, por lo que tienes un notable.")

    case 9 | 10:
        print(f"Tu nota es {nota}, por lo que tienes un sobresaliente.")

    case _:
        print("Error")


nota2 = int(input("Ingresa tu segunda nota: "))

if nota2 < 0 or nota2 > 10:
    print("Tu nota no es válida.")

else:

    if nota2 in [1, 2, 3, 4]:
        print(f"Tienes un {nota2}, por lo que has suspendido.")

    elif nota2 in [5, 6]:
        print(f"Tines un {nota2}, por lo que tienes un suficiente.")

    elif nota2 in [7, 8]:
        print(f"Tienes un {nota2}, por lo que tienes un notable.")

    elif nota2 in [9, 10]:
        print(f"Tienes un {nota2}, por lo que tienes un sobresaliente.")