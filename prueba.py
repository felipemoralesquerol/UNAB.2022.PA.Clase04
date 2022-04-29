class Animal():
    nombre = 'a definir'
    pass

class Gato(Animal):
    cantidad_patas = 4
    pass


# Invocaciones
a = Animal()
g = Gato()
print(a.nombre)
print(g.cantidad_patas)
x = object()
print(type(x))


