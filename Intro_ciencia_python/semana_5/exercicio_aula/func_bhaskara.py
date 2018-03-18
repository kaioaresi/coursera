import math
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

def delta(a,b,c):
	d = b ** 2 - 4 * a * c
	return d

def raiz_delta():
	raiz_delta = math.sqrt(delta(a,b,c))
	return raiz_delta

def bhaskara(a,b,c):
	x1 = (- b + raiz_delta()) / (2 * a)
	x2 = (- b - raiz_delta()) / (2 * a)

if delta(a,b,c) == 0:
	x1 = (- b + raiz_delta()) / (2 * a)
	print('a raiz desta equação é {}'.format(x1))
else:
	if delta(a,b,c) < 0:
		print('esta equação não possui raízes reais')
	else:
		x1 = (- b + raiz_delta()) / (2 * a)
		x2 = (- b - raiz_delta()) / (2 * a)
		if x1 > x2:
			print('as raízes da equação são {} e {}'.format(x2, x1))
		else:
			print('as raízes da equação são {} e {}'.format(x1, x2))