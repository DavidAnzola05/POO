class Vehiculo:
    """Nivel 1: Base más general"""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado")


class VehiculoTerrestre(Vehiculo):
    """Nivel 2: Especialización media"""
    def __init__(self, marca, modelo, num_ruedas):
        super().__init__(marca, modelo)
        self.num_ruedas = num_ruedas

    def frenar(self):
        print(f"Frenando con {self.num_ruedas} ruedas")


class Automovil(VehiculoTerrestre):
    """Nivel 3: Especialización alta"""
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo, 4)
        self.num_puertas = num_puertas

    def abrir_puerta(self, numero):
        if 1 <= numero <= self.num_puertas:
            print(f"Abriendo puerta {numero}")
        else:
            print(f"Puerta {numero} no existe")


class Motocicleta(VehiculoTerrestre):
    """Nivel 3: Otra especialización"""
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, 2)
        self.tipo = tipo

    def hacer_caballito(self):
        if self.tipo == "deportiva":
            print("¡Haciendo caballito!")
        else:
            print("Esta moto no hace caballitos")


auto = Automovil("Toyota", "Corolla", 4)
moto = Motocicleta("Yamaha", "R1", "deportiva")

auto.encender()
auto.frenar()
auto.abrir_puerta(1)

moto.encender()
moto.frenar()
moto.hacer_caballito()

print(f"\n¿Auto es Vehiculo? {isinstance(auto, Vehiculo)}")
print(f"¿Auto es VehiculoTerrestre? {isinstance(auto, VehiculoTerrestre)}")
print(f"¿Auto es Automovil? {isinstance(auto, Automovil)}")
print(f"¿Moto es Automovil? {isinstance(moto, Automovil)}")
    