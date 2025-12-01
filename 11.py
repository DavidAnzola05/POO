from abc import ABC, abstractmethod
import math

# Clase base abstracta
class Figura(ABC):
    """Clase base para todas las figuras geométricas"""

    def __init__(self, color="Blanco"):
        self.color = color

    @abstractmethod
    def area(self):
        """Método abstracto - cada figura debe implementarlo"""
        pass

    @abstractmethod
    def perimetro(self):
        """Método abstracto - cada figura debe implementarlo"""
        pass

    def describir(self):
        """Método común para todas las figuras"""
        return f"{self.__class__.__name__} {self.color}"

    def info_completa(self):
        """Método que usa métodos polimórficos"""
        print(f"\n{self.describir()}")
        print(f" Área: {self.area():.2f} unidades2")
        print(f" Perímetro: {self.perimetro():.2f} unidades")


class Circulo(Figura):
    def __init__(self, radio, color="Blanco"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        """Método específico de Círculo"""
        return 2 * self.radio


class Rectangulo(Figura):
    def __init__(self, ancho, alto, color="Blanco"):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        """Método específico de Rectángulo"""
        return self.ancho == self.alto


class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, color="Blanco"):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def tipo_triangulo(self):
        """Método específico de Triángulo"""
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


# POLIMORFISMO
def calcular_area_total(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def imprimir_info_figuras(figuras):
    for figura in figuras:
        figura.info_completa()


def comparar_figuras(figura1, figura2):
    area1 = figura1.area()
    area2 = figura2.area()

    print(f"\nComparando {figura1.describir()} vs {figura2.describir()}")
    if area1 > area2:
        print(f" {figura1.describir()} es mayor")
    elif area1 < area2:
        print(f" {figura2.describir()} es mayor")
    else:
        print(" Ambas tienen la misma área")


# Crear diferentes figuras
figuras = [
    Circulo(5, "Rojo"),
    Rectangulo(4, 6, "Azul"),
    Triangulo(3, 4, 5, "Verde"),
    Circulo(3, "Amarillo"),
    Rectangulo(5, 5, "Morado")  # Cuadrado
]

# DEMOSTRACIÓN
print("="*60)
print("DEMOSTRACIÓN DE POLIMORFISMO")
print("="*60)

imprimir_info_figuras(figuras)

print(f"\n{'='*60}")
print(f"Área total de todas las figuras: {calcular_area_total(figuras):.2f} unidades2")

comparar_figuras(figuras[0], figuras[1])
comparar_figuras(figuras[2], figuras[3])

print(f"\n{'='*60}")
print("ANÁLISIS DE FIGURAS")
print("="*60)

for i, figura in enumerate(figuras, 1):
    print(f"\n{i}. {figura.describir()}")
    print(f" Área: {figura.area():.2f}")
    print(f" Perímetro: {figura.perimetro():.2f}")

    if isinstance(figura, Circulo):
        print(f" Diámetro: {figura.diametro():.2f}")
    elif isinstance(figura, Rectangulo):
        print(f" ¿Es cuadrado? {figura.es_cuadrado()}")
    elif isinstance(figura, Triangulo):
        print(f" Tipo: {figura.tipo_triangulo()}")
