# Función decoradora
def calcular_area_triangulo(function):
    # Función de retorno
    def funcion_de_retorno(*args, **kwargs):
        #print(*args)
        res = function(*args, **kwargs)
        return res / 2

    return funcion_de_retorno

# Uso de decorador
@calcular_area_triangulo
def calcular_area(base, altura):
    return base * altura

# Invocación
if __name__ == "__main__":
    print(calcular_area(4, 10))