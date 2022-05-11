class Animal():
    nombre = 'a definir'

    def piel(self):
        return "piel a definir"
   

class Gato(Animal):
    cantidad_patas = 4

    def piel(self):
        return super().piel()


# Invocaciones
a = Animal()
g = Gato()

print(g.cantidad_patas)
print(g.piel())