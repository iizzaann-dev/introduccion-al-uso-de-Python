lista = [1, 2, 3]
print(lista)
print("Primero: ", lista[0])
print("Último: ", lista[-1])

producto = [2, "TV LG", 12]
print(producto)

listaA = ["A", "B"]
listaB = ["C", "D"]
listaA.extend(listaB)
listaA.extend(["E", "F"])
listaA.append("G")
print(listaA)
del listaA[0]
print(listaA)

tupla = (1, 2, 3)
print(tupla)
print(tupla[1])

rango = range(1,20,2)
print(rango[4])
print("Rango:", rango[1])

inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el final del rango: "))
rango = range(inicio, fin)
print(rango[2])

diccionario = {
    "titulo" : "Crash Bandicoot",
    "consola" : "PS3",
    "precio" : 59.95
}

print(diccionario)
print(diccionario["titulo"])
