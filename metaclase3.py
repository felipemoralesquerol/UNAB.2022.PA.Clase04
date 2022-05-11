# Ejemplos de herencia múltiple
Animal = type('Animal', (), {'nombre':'Animal a definir'})

Vegetal = type('Vegetal', (), {'nombre_veg':'Vegetal a definir'})

def dice(self):
    print('Guauuuuuu!')

Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))


Hatana = type('Hatana', (Vegetal,Animal, ), dict())

# Operaciones con clase Perro
print('Operaciones sobre Perro')
p = Perro()
print(p.nombre)          # Imprime a definir
print(p.cantidad_patas)  # Imprime 4
p.dice()                 # Imprime Guauuuuuu
print()

# Operaciones con clase Hatana
print('Operaciones sobre Hatana')
h = Hatana()
print(h.nombre)
print(h.nombre_veg)

