n = int(input('Digite um número inteiro: '))

check = n % 2


if check == 1 and n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
	print('primo'.format(check))
else:
	print('não primo'.format(check))