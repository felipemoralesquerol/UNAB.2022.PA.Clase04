class Animal():
    nombre = 'Soy un animal'
    pass


class Gato(Animal):
    cantidad_patas = 4
    pass


# Invocaciones
# Creación de instancias
a = Animal()
g = Gato()

# Impresiones
print(a.nombre)
print(g.cantidad_patas)

# Referencias
x = object()
print(type(x))

# Determina si x es una instancia de object
print(isinstance(x ,object))




