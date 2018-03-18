n = int(input('Digite um número inteiro: '))

def adjacente(numero):
	while numero != 0:
		aux = numero % 10
		print('aux ', aux)
	
		adj = aux
		print('adj', adj)
		numero //= 10


adjacente(n)