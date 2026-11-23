def sumatorio(a:int) -> int:
    acumulador = 0
    if a >= 0:
        for i in range(0, a):
            acumulador += 1
            print(acumulador)
    
    
def factorial(a:int) -> int:
    multiplicador = 1
    
    if a >= 0:
        for i in range(1, a+1):
            multiplicador *= i
            print(multiplicador)
            

def aplicar_funcion(b:int, frase:str):
    
    frase = frase.lower().strip()
    
    if frase == "sumatorio":
        sumatorio(b)
        
    if frase == "factorial":
        factorial(b)
    
    
    
aplicar_funcion(3, "factorial")
aplicar_funcion(10, "sumatorio")