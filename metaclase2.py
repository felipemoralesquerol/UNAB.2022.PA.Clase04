Animal = type('Animal', (), {'nombre':'Animal a definir'})


def dice(self):
    print('Guauuuuuu')


Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))


print('Perro')
p = Perro()
print(p.nombre)          # Imprime a definir
print(p.cantidad_patas)  # Imprime 4
p.dice()                 # Imprime Guauuuuuu
