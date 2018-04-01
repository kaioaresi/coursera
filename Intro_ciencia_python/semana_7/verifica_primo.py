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


def recebe_numero():
	n = int(input('Digite um número: '))

	while n >= 1:
		if checK_primo(n):
			print('O número {} é primo'.format(n))
		else:
			print('O número {} NÃO é primo'.format(n))
		n = int(input('Digite um número: '))

recebe_numero()