class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        print(f"Calculando salario base para {self.nombre}")
        return self.salario_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario base: ${self.salario_base}")


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        salario = super().calcular_salario()
        print(f"Agregando bono de gerente: ${self.bono}")
        return salario + self.bono

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Bono: ${self.bono}")
        print(f"Salario total: ${self.calcular_salario()}")


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comision_porcentaje):
        super().__init__(nombre, salario_base)
        self.comision_porcentaje = comision_porcentaje
        self.ventas_mes = 0

    def registrar_venta(self, monto):
        self.ventas_mes += monto
        print(f"Venta registrada: ${monto}")

    def calcular_salario(self):
        salario = super().calcular_salario()
        comision = self.ventas_mes * (self.comision_porcentaje / 100)
        print(f"Agregando comisión por ventas: ${comision}")
        return salario + comision

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Comisión: {self.comision_porcentaje}%")
        print(f"Ventas del mes: ${self.ventas_mes}")
        print(f"Salario total: ${self.calcular_salario()}")


gerente = Gerente("Ana García", 3000, 1000)
vendedor = Vendedor("Carlos López", 1500, 10)

print("=" * 50)
gerente.mostrar_info()

print("\n" + "=" * 50)
vendedor.registrar_venta(5000)
vendedor.registrar_venta(3000)
vendedor.mostrar_info()
