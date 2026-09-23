def main():
    fruta1 = ["Manzana", "Pera", "Melocotón"]
    fruta2 = ["Kiwi", "Sandía", "Melón"]

    fruta1.extend(fruta2)

    print(fruta2[-1])

    tupla = (3, 5, 7)

    print(tupla[0])

    inicio = int(input("Ingresa el inicio del rango: "))
    fin = int(input("Ingresa el final del rango: "))
    salto = int(input("Ingresa el salto de rango: "))

    rango = range(inicio, fin, salto)
                
    print(rango)

main()