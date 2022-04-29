class Animal():
    nombre = 'a definir'
    pass

class Gato(Animal):
    cantidad_patas = 4
    pass



# Invocaciones
a = Animal()
g = Gato()

print(g.cantidad_patas)

# Usando metaclases
GatoMC = type('GatoMC', (Animal, ),{'cantidad_patas':4})

gMC = GatoMC()
print(gMC.cantidad_patas, gMC.nombre)
print(type(gMC))