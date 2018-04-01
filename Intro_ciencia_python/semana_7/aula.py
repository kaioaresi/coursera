# repetições encaixadas
# tabuada

def tabuada():
	x = 1
	y = 1
	while x <= 10:
		print()
		print('Tabuada do ', x)
		print('===' * 4)

		while y <= 10:
			print('{} X {} = {}'.format(x,y,x * y))
			y += 1

		x += 1
		y = 1


tabuada()