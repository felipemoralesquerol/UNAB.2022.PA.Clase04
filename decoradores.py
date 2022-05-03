def my_primer_decorador(function):
	def funcion_de_retorno():
		print('Cargando...')
		function()
		print('Proceso finalizado')

	return funcion_de_retorno


@my_primer_decorador
def funcion_de_entrada():
	print('Hola mundo')


if __name__ == "__main__":
    funcion_de_entrada()