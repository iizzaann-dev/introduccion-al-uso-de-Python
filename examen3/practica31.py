euro_dolar = 1.10
euro_libra = 0.83
dolar_euro = 0.91
dolar_libra = 0.76
libra_euro = 1.20
libra_dolar = 1.32

nvda = 156.20
sony = 24.16
bmw = 58.12

def convertir_acciones(compania: str, num_acciones: int, moneda: str):

    compania = compania.lower()
    moneda = moneda.lower()

    if compania == "nvda": 
        if moneda == "euro":
            return round((nvda * num_acciones), 2)

        elif moneda == "dolar":
            return round((num_acciones * euro_dolar * nvda) ,2)

        elif moneda == "libra":
            return round((num_acciones * euro_libra * nvda) ,2)

    elif compania == "sony":
        if moneda == "euro":
            return round((sony * num_acciones), 2)

        elif moneda == "dolar":
            return round((num_acciones * euro_dolar * sony), 2)

        elif moneda == "libra":
            return round((num_acciones * euro_libra * sony), 2)

    elif compania == "bmw": 
        if moneda == "euro":
            return round((bmw * num_acciones), 2)

        elif moneda == "dolar":
            return round((num_acciones * euro_dolar * bmw), 2)

        elif moneda == "libra":
            return round((num_acciones *euro_libra * bmw), 2)


print(convertir_acciones("NVDA", 10, "euro"))
print(convertir_acciones("SONY", 5, "dolar"))
print(convertir_acciones("BMW", 20, "libra"))
