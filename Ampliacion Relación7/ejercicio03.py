euro_dolar = 1.09
euro_yen = 163.38
dolar_euro = 0.92
dolar_yen = 149.67
yen_euro = 0.0061
yen_dolar = 0.0067




def cambiar_divisa(divisa: float, cadena:str, cadena2:str) -> float:
    
    resultado = 0
    cadena = cadena.lower().strip()
    cadena2 = cadena2.lower().strip()
    
    if cadena == cadena2:
        resultado = divisa
    
    if divisa < 0: 
        raise ValueError("La cantidad ingresada es negativa")
    
    else:
        
        if cadena in ["dolar", "euro", "yen", "dolares", "euros", "yenes"] and cadena2 in ["dolar", "euro", "yen", "dolares", "euros", "yenes"]:
            
            if cadena == "euro" or cadena == "euros":
                if cadena2 == "dolar" or cadena2 == "dolares":
                    resultado = divisa * euro_dolar
                
                elif cadena2 == "yen" or cadena2 == "yenes":
                    resultado = divisa * euro_yen
                
            elif cadena == "dolar" or cadena == "dolares":
                
                if cadena2 == "euro" or cadena2 == "euros":
                    resultado = divisa * dolar_euro
                
                elif cadena2 == "yen" or cadena2 == "yenes":
                    resultado = divisa * dolar_yen
                    
            elif cadena == "yen" or cadena == "yenes":
                
                if cadena2 == "euro" or cadena2 == "euros":
                    resultado = divisa * yen_euro
                    
                elif cadena2 == "dolar" or cadena2 == "dolares":
                    resultado = divisa * yen_dolar
                
        else:
            raise ValueError("No existe la divisa ingresada")
        
    return round(resultado)


print(cambiar_divisa(10, "euro", "dolar"))
