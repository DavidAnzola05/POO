# Nivel 1: Base más general
class Persona:
    def __init__(self, nombre, edad, identificacion):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre es obligatorio")
        if edad < 18:
            raise ValueError("Debe ser mayor de edad")

        self.nombre = nombre.strip()
        self.edad = edad
        self.identificacion = identificacion

    def mostrar_info(self):
        print(f"{'='*50}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"ID: {self.identificacion}")


# Nivel 2: Empleado general
class Empleado(Persona):
    contador_empleados = 0

    def __init__(self, nombre, edad, identificacion, departamento, fecha_ingreso):
        super().__init__(nombre, edad, identificacion)
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso

        Empleado.contador_empleados += 1
        self.numero_empleado = f"EMP-{Empleado.contador_empleados:04d}"

    def calcular_salario_mensual(self):
        raise NotImplementedError("Cada tipo de empleado debe implementar este método")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Empleado: {self.numero_empleado}")
        print(f"Departamento: {self.departamento}")
        print(f"Fecha de Ingreso: {self.fecha_ingreso}")


# Nivel 3: Tiempo Completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, edad, identificacion, departamento, fecha_ingreso, salario_mensual):
        super().__init__(nombre, edad, identificacion, departamento, fecha_ingreso)

        if salario_mensual <= 0:
            raise ValueError("El salario debe ser positivo")

        self.salario_mensual = salario_mensual

    def calcular_salario_mensual(self):
        return self.salario_mensual

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: Tiempo Completo")
        print(f"Salario Mensual: ${self.salario_mensual:,.2f}")


# Nivel 3: Por Horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, identificacion, departamento, fecha_ingreso, tarifa_hora):
        super().__init__(nombre, edad, identificacion, departamento, fecha_ingreso)

        if tarifa_hora <= 0:
            raise ValueError("La tarifa debe ser positiva")

        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = 0

    def registrar_horas(self, horas):
        if horas < 0:
            raise ValueError("Las horas no pueden ser negativas")
        self.horas_trabajadas += horas
        print(f"Registradas {horas} horas. Total: {self.horas_trabajadas}")

    def calcular_salario_mensual(self):
        salario = self.horas_trabajadas * self.tarifa_hora

        if self.horas_trabajadas > 160:
            horas_extra = self.horas_trabajadas - 160
            extra = horas_extra * self.tarifa_hora * 0.5
            salario += extra
            print(f" Horas extra: {horas_extra} (+${extra:,.2f})")

        return salario

    def reiniciar_horas(self):
        self.horas_trabajadas = 0

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: Por Horas")
        print(f"Tarifa por Hora: ${self.tarifa_hora:,.2f}")
        print(f"Horas Trabajadas (mes actual): {self.horas_trabajadas}")


# Nivel 4: Gerente
class Gerente(EmpleadoTiempoCompleto):
    def __init__(self, nombre, edad, identificacion, departamento, fecha_ingreso,
                 salario_mensual, bono_anual):
        super().__init__(nombre, edad, identificacion, departamento, fecha_ingreso,
                         salario_mensual)
        self.bono_anual = bono_anual
        self.equipo = []

    def agregar_empleado_equipo(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("Debe ser un Empleado")
        if empleado not in self.equipo:
            self.equipo.append(empleado)
            print(f"{empleado.nombre} agregado al equipo de {self.nombre}")

    def calcular_salario_mensual(self):
        salario_base = super().calcular_salario_mensual()
        bono_mensual = self.bono_anual / 12
        return salario_base + bono_mensual

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Posición: GERENTE")
        print(f"Bono Anual: ${self.bono_anual:,.2f}")
        print(f"Empleados a Cargo: {len(self.equipo)}")
        if self.equipo:
            print("Equipo:")
            for emp in self.equipo:
                print(f" - {emp.nombre} ({emp.numero_empleado})")


# DEMOSTRACIÓN COMPLETA
print("SISTEMA DE GESTIÓN DE EMPLEADOS")
print("="*50)

emp1 = EmpleadoTiempoCompleto(
    "Ana García", 30, "ID-001",
    "Contabilidad", "2020-01-15", 3000
)

emp2 = EmpleadoPorHoras(
    "Carlos López", 25, "ID-002",
    "Soporte Técnico", "2021-06-01", 15
)

gerente = Gerente(
    "María Torres", 40, "ID-003",
    "Ventas", "2018-03-10", 5000, 12000
)

emp2.registrar_horas(80)
emp2.registrar_horas(90)

gerente.agregar_empleado_equipo(emp1)
gerente.agregar_empleado_equipo(emp2)

print("\n")
emp1.mostrar_info()
print(f"Salario Mensual: ${emp1.calcular_salario_mensual():,.2f}")

print("\n")
emp2.mostrar_info()
print(f"Salario Mensual: ${emp2.calcular_salario_mensual():,.2f}")

print("\n")
gerente.mostrar_info()
print(f"Salario Mensual: ${gerente.calcular_salario_mensual():,.2f}")

print("\n" + "="*50)
print("VERIFICACIÓN DE JERARQUÍA")
print("="*50)
print(f"¿Gerente es Persona? {isinstance(gerente, Persona)}")
print(f"¿Gerente es Empleado? {isinstance(gerente, Empleado)}")
print(f"¿Gerente es EmpleadoTiempoCompleto? {isinstance(gerente, EmpleadoTiempoCompleto)}")
print(f"¿Gerente es EmpleadoPorHoras? {isinstance(gerente, EmpleadoPorHoras)}")

print(f"\nTotal de empleados creados: {Empleado.contador_empleados}")
