n = int(input('Digite um número inteiro: '))

check = n % 2


if check == 1:
	print('primo'.format(check))
else:
	print('não primo'.format(check))