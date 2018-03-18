import math

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = b ** 2 - 4 * a * c


if delta == 0:
	raiz_delta = math.sqrt(delta)
	x1 = (- b + raiz_delta) / (2 * a)
	print('a raiz desta equação é {}'.format(x1))

else:

	if delta < 0:
		print('esta equação não possui raízes reais')
	else:
		raiz_delta = math.sqrt(delta)
		x1 = (- b + raiz_delta) / (2 * a)
		x2 = (- b - raiz_delta) / (2 * a)
		if x1 > x2:
			print('as raízes da equação são {} e {}'.format(x2, x1))
		else:
			print('as raízes da equação são {} e {}'.format(x1, x2))
