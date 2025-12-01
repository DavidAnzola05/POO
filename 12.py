class CuentaBancariaDAAC:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__historial = []

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad
        self.__historial.append(f"Depósito: +${cantidad}")
        return True

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= cantidad
        self.__historial.append(f"Retiro: -${cantidad}")
        return True

    @property
    def historial(self):
        return self.__historial.copy()


cuentaDAAC = CuentaBancariaDAAC("Ana García", 1000)

print(f"Saldo actual: ${cuentaDAAC.saldo}")

cuentaDAAC.depositar(500)
cuentaDAAC.retirar(200)

for trans in cuentaDAAC.historial:
    print(trans)

hist = cuentaDAAC.historial
hist.append("Hack")

print(len(cuentaDAAC.historial))
