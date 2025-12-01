class PerroDAAC:
    def __init__(self):
        self.nombre = "Sin nombre" 
        self.edad = 0
        self.color = "marrón" 
        self.energia = 100
Mi_perro = PerroDAAC()
print(f"Mi perro: {Mi_perro}")
print(f"Mi perro tiene el nombre: {Mi_perro.nombre}")
print(f"Mi perro tiene {Mi_perro.edad} años")
print(f"Mi perro es {Mi_perro.color}")
print(f"Mi perro tiene {Mi_perro.energia} de energía")
Mi_perro.nombre = "Rex"
Mi_perro.edad = 5
Mi_perro.color = "Amarillo"
Mi_perro.energia = 1000
 
print(f"Mi perro tiene el nombre: {Mi_perro.nombre}")
print(f"Mi perro tiene {Mi_perro.edad} años")
print(f"Mi perro es {Mi_perro.color}")
print(f"Mi perro tiene {Mi_perro.energia} de energía")