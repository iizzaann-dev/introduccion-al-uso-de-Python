def convertirTemperatura(num: float, a: str, b: str):
    a = a.upper()
    b = b.upper()

    match a:
        case "C":
            celsius = num
        case "F":
            celsius = (num - 32) * 5/9
        case "K":
            celsius = num - 273.15
        case _:
            print("Unidad de origen no válida.")
            return

    match b:
        case "C":
            return celsius
        case "F":
            return (celsius * 9/5) + 32
        case "K":
            return celsius + 273.15
        case _:
            print("Unidad de destino no válida.")
            return
        

print(round(convertirTemperatura(23.56, "c", "f"), 2))