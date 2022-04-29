# Ejemplos de herencia múltiple
Animal = type('Animal', (), {'nombre':'Animal a definir'})

Vegetal = type('Vegental', (), {'nombrev':'Vegetal a definir'})

def dice(self):
    print('Guauuuuuu')


Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))
Hatana = type('Hatana', (Animal, Vegetal, ), dict())

print('Perro')
p = Perro()
print(p.nombre)          # Imprime a definir
print(p.cantidad_patas)  # Imprime 4
p.dice()                 # Imprime Guauuuuuu

print('Hatana')
h = Hatana()
print(h.nombre)