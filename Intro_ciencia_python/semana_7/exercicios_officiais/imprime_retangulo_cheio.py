'''
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
'''
def h_altura(altura):
	i = 1
	while altura >= i:
		print('#',end='')
		i += 1

altura = int(input('Digite a altura: '))
largura = int(input('Digite a largura: '))

j = 1
while largura >= j:
	h_altura(altura)
	print()
	j += 1
	