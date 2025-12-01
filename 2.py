class PerroGoldenGateDavid:
    pass

firulais = PerroGoldenGateDavid() 
bobby = PerroGoldenGateDavid() 
lassie = PerroGoldenGateDavid() 

print(f"Firulais: {firulais}")
print(f"Bobby: {bobby}")
print(f"Lassie: {lassie}")

print(f"\nID de Firulais: {id(firulais)}")
print(f"ID de Bobby: {id(bobby)}")
print(f"ID de Lassie: {id(lassie)}")

print(f"\n¿Firulais y Bobby son el mismo? {firulais is bobby}") 
print(f"¿Todos son de tipo Perro? {isinstance(firulais, PerroGoldenGateDavid)}") 