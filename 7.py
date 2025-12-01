class AnimalDAAC:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido")

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        self.hacer_sonido()


class PerroDAAC(AnimalDAAC):
    def hacer_sonido(self):
        print(f"{self.nombre} ¡Guau guau!")


class GatoDAAC(AnimalDAAC):
    def hacer_sonido(self):
        print(f"{self.nombre} ¡Miau miau!")


class VacaDAAC(AnimalDAAC):
    def hacer_sonido(self):
        print(f"{self.nombre} ¡Muuu!")


animales = [
    AnimalDAAC("Genérico"),
    PerroDAAC("Max"),
    GatoDAAC("Luna"),
    VacaDAAC("Lola")
]

for animal in animales:
    animal.presentarse()
    print()