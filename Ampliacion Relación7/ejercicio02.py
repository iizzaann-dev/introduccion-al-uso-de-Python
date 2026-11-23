from datos import animales

def comprobar_estado(nombre:str) -> str:
    
    nombre = nombre.lower().strip()
    nombres = [i[0].lower().strip() for i in animales]
    
    if nombre in nombres:
        for i in animales:
            if i[0].lower().strip() == nombre:
                if i[2] == 0:
                    print("Extinto")
                    
                elif i[2] > 0 and i[2] <= 500:
                    print("En peligro crítico")
                    
                elif i[2] > 500 <= 2000:
                    print("En peligro")
                
                elif i[2] > 2000:
                    print("Amenazado")
    else:
        raise ValueError(f"No se encuentra al animal ({nombre}) dentro de la lista." )
    
comprobar_estado("Lobo ibérico")