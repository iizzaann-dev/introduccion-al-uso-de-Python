class cuentaBancaria: 
    def __init__(self, nombre: str, saldo: float = 0.0):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.nombre = nombre
        self.saldo = saldo
        
    def ingresar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a ingresar no puede ser menor de 0")
        
        self.saldo += cantidad
        
    def retirar(self, cantidad : float):
        if cantidad < 0:
            raise ValueError("La cantidad a retirar no puede ser negativa")
        
        if cantidad > self.saldo:
            raise ValueError("La cantidad a retirar no puede ser mayor que el saldo de la cuenta")
        
        self.saldo -= cantidad
        
    def __str__(self):
        return f"CuentaBancaria[nombre={self.nombre} | Saldo={self.saldo}]"
    
    
cuenta1 = cuentaBancaria("Juan")
cuenta2 = cuentaBancaria("María", 500.0)

print(cuenta1)
print(cuenta2)

cuenta1.ingresar(200)
cuenta2.retirar(100)
print(cuenta1)
print(cuenta2)