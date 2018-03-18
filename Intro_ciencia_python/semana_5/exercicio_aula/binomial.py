

n = int(input('Digite o valor N: '))
k = int(input('Digite o valor K: '))


def fatorial(numero):
	x = numero
	f = 1

	while x > 0:
		f *= x
		x -= 1
		
	return f

'''
 n! / k!(n - k)!
'''
def binomial(n, k):
	return fatorial(n) // (fatorial(k) * (fatorial(n - k)))


def test_binomial():
	if binomial(20, 10) == 184756:
		print('Teste 20 e 10 correto')
	else:
		print('Teste 20 e 10 incorreto.')


print(binomial(n, k))