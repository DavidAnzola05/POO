class personaDAAC:
    def __init__(self, nombre,):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
juan = personaDAAC("Juan")
juan.saludar()
maria = personaDAAC("María")
maria.saludar()