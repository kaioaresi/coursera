def computador_escolhe_jogada(qtd_pecas, qat_movimentos):
	# n quantidade de peças e m quantidade de movimentos
	pc = 1

	while pc != qat_movimentos:
		if (qtd_pecas - pc) % (m + 1) == 0:
			return pc

		else:
			pc += 1
	return pc





def partida():
	
	# verificar se n multiplo de m, se sim jogador começa, caso contrario o computador começa
	n = int(input('Quantas peças? '))
	m = int(input('Limite de peças por jogada? '))

	if n % (m + 1) == 0:
		print('Jogador começa!')
	else:
		print('Computador começa!')




n = int(input('Quantas peças? '))
m = int(input('Limite de peças por jogada? '))

computador_escolhe_jogada(n, m)