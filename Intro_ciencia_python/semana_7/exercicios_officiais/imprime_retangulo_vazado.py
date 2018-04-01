'''
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''

def h_altura(largura):
	i = 1
	while largura >= i:
		print('#',end='')
		i += 1

def checK_primo(numero):
	check = 2

	if numero == 2:
		return True

	while numero % check != 0 and check <= numero / 2:
		check += 1
	if numero % check == 0:
		return False
	else:
		return True


def v_altura(largura, altura):
	i = 1
	j = 1

	if checK_primo(largura):
		h_altura(largura)
		print()
		while largura >= i:
			if largura % j == 0:
				print('#', end='')				
			else:
				print(' ', end='')
			i += 1
			j += 1
		print()
		h_altura(largura)
	else:		
		h_altura(largura)
		print()
		print('#', end='')
		while ( largura - 2) >= i:
			if largura % j != 0:				
				print(' ', end='')
				i += 1
			else:
				print(end=' ')
				i += 1
		print('#', end='')
		print()
		h_altura(largura)

			
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
if largura == 2 and altura == 2:
	j = 1
	while largura >= j:
		h_altura(altura)
		print()
		j += 1
else:
	v_altura(largura, altura)