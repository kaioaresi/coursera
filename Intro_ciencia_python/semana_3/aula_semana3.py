# Condicionais
'''
# exercicio
# https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_quadr%C3%A1tica

O programa recebera três valores, a, b e c, utilize a formula de bascara e imprima as raizes, 

Resultados:
Se delta < 0:
	não tem raiz reais

Se delta == 0
	tem uma raiz real que é X
Se delta > 0
	escrever as duas raizes reais x e y

# formula de bhaskara

x = -b +/- ^delta
	-------------
		2a

delta = b² - 4.a.c
'''
import math

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = b ** 2 - 4 * a * c


if delta == 0:
	raiz_delta = math.sqrt(delta)
	x1 = (- b + raiz_delta) / (2 * a)
	print('Delta tem uma raiz real que é {}'.format(x1))

else:

	if delta < 0:
		print('Delta não tem raiz reais'.format(delta))
	else:
		raiz_delta = math.sqrt(delta)
		x1 = (- b + raiz_delta) / (2 * a)
		x2 = (- b - raiz_delta) / (2 * a)
		print('Delta tem duas raizes reais o sendo elas:\nx1 = {}\nx2 = {}'.format(x1, x2))

