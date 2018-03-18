import math

xa = int(input('Digite um ponto XA: '))
ya = int(input('Digite outro ponto YA: '))

xb = int(input('Digite nova outr ponto XB: '))
yb = int(input('Digite mais um ponto YB: '))

dab = math.sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))

if dab > 10:
	print('longe {}'.format(dab))
else:
	print('perto {}'.format(dab))
