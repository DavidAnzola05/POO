class PerroGoldenGateDavid:
    pass
perro1 = PerroGoldenGateDavid()
perro2 = PerroGoldenGateDavid()

print(id(perro1)) 
print(id(perro2)) 

print(perro1 == perro2)  
print(perro1 is perro2)  
print(type(perro1) == type(perro2))  