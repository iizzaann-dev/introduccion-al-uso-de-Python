def calcularValorBruto(num: float, iva: str) -> float:
    
    iva = iva.lower()
    
    if iva == "general":
        num = num * 1.21
        return num
    
    elif iva == "reducido":
        num = num * 1.10
        return num
    
    elif iva == "superreducido":
        num = num * 1.04
        return num
    
    else:
        return("Iva no válido.")
        
print(round(calcularValorBruto(10, "general")))
    
    