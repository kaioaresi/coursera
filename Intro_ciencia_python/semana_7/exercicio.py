# receba vários número do usuário e retorne o fatorial de cada uma deles, quando o usuário digitar '0' para o programa
def fatorial(n):
	f = 1
	while n > 0:
		f = f * n
		n -= 1
	return f

def multiplos_numeros():
	n = int(input('Digite um número: '))
	while n >= 0:
		print('O fatorial deste número {} é {}'.format(n, fatorial(n)))
		n = int(input('Digite um número: '))

multiplos_numeros()