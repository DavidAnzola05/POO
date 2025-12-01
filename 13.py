import re
from datetime import datetime

class PersonaDAAC:
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.__fecha_creacion = datetime.now()
        self.__modificaciones = 0

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser un texto no vacío")
        valor = valor.strip()
        if len(valor) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        if len(valor) > 50:
            raise ValueError("El nombre no puede tener más de 50 caracteres")
        if not all(c.isalpha() or c.isspace() for c in valor):
            raise ValueError("El nombre solo puede contener letras y espacios")
        self.__nombre = valor
        self.__modificaciones += 1

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El email es obligatorio")
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor):
            raise ValueError("Formato de email inválido")
        self.__email = valor.lower().strip()
        self.__modificaciones += 1

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La edad debe ser un número entero")
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        if valor > 150:
            raise ValueError("La edad no puede ser mayor a 150")
        self.__edad = valor
        self.__modificaciones += 1

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    @property
    def modificaciones(self):
        return self.__modificaciones

    def cumpleaños(self):
        self.__edad += 1
        print(f"¡Feliz cumpleaños {self.__nombre}! Ahora tienes {self.__edad} años")

    def cambiar_email(self, nuevo_email):
        email_anterior = self.__email
        self.email = nuevo_email
        print(f"Email cambiado de {email_anterior} a {self.__email}")

    def __str__(self):
        return f"{self.__nombre} ({self.__edad} años) - {self.__email}"

    def info_completa(self):
        print(f"\n{'='*50}")
        print("INFORMACIÓN DE PERSONA")
        print(f"{'='*50}")
        print(f"Nombre: {self.__nombre}")
        print(f"Email: {self.__email}")
        print(f"Edad: {self.__edad} años")
        print(f"Fecha de creación: {self.__fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Modificaciones: {self.__modificaciones}")
        print(f"{'='*50}\n")


print("DEMOSTRACIÓN DAAC\n")

try:
    personaDAAC = PersonaDAAC("Ana García", "ana@email.com", 25)
    print("Persona creada")
    personaDAAC.info_completa()
except ValueError as e:
    print(f"Error: {e}")

personaDAAC.nombre = "Ana María García"
personaDAAC.edad = 26
personaDAAC.cambiar_email("anamaria@email.com")

personaDAAC.info_completa()

try:
    personaDAAC.nombre = ""
except ValueError as e:
    print(f"Nombre rechazado: {e}")

try:
    personaDAAC.email = "email_invalido"
except ValueError as e:
    print(f"Email rechazado: {e}")

try:
    personaDAAC.edad = -5
except ValueError as e:
    print(f"Edad rechazada: {e}")

try:
    personaDAAC.edad = "treinta"
except TypeError as e:
    print(f"Edad rechazada: {e}")

try:
    personaDAAC.fecha_creacion = datetime.now()
except AttributeError:
    print("No se puede modificar fecha_creacion")

try:
    personaDAAC.modificaciones = 0
except AttributeError:
    print("No se puede modificar modificaciones")

personaDAAC.cumpleaños()
personaDAAC.info_completa()

print("Intentando acceso directo...")
try:
    print(personaDAAC.__nombre)
except AttributeError:
    print("No puedes acceder a __nombre directamente")

print(f"Correcto: {personaDAAC.nombre}")
print(f"Total modificaciones: {personaDAAC.modificaciones}")