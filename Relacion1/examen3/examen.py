def convertir_acciones(compania, numero_acciones, moneda_cambio):
    """
    Calcula el valor de un número de acciones y lo convierte
    a la moneda indicada.

    :param compania: Código de la compañía (NVDA, SONY o BMW).
    :param numero_acciones: Número de acciones.
    :param moneda_cambio: Moneda de destino (euro, dolar o libra).
    :return: Valor total convertido, redondeado a dos decimales.
    """

    # Valor de cada acción expresado en euros
    acciones = {
        "NVDA": 156.20,
        "SONY": 24.16,
        "BMW": 58.12
    }

    # Factores de conversión desde euros
    monedas = {
        "euro": 1,
        "dolar": 1.10,
        "libra": 0.83
    }

    # Admitir compañías y monedas escritas en mayúsculas o minúsculas
    compania = compania.upper()
    moneda_cambio = moneda_cambio.lower()

    # Calcular el valor total de las acciones en euros
    valor_total = acciones[compania] * numero_acciones

    # Convertir el importe a la moneda solicitada
    resultado = valor_total * monedas[moneda_cambio]

    return round(resultado, 2)


# Ejemplos de comprobación indicados en el examen
if __name__ == "__main__":
    print(convertir_acciones("NVDA", 10, "euro"))   # 1562.0
    print(convertir_acciones("SONY", 5, "dolar"))   # 132.88
    print(convertir_acciones("BMW", 20, "libra"))   # 964.79
