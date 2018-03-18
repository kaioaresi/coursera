def computador_escolhe_jogada(n,m):
	
	if m <= n:
		return m		
	else:
		estrategia_win = (m + 1) % n # se m não multiplo de n

		if estrategia_win > 0 and estrategia_win <= m:
			return estrategia_win
		else:
			return m

def usuario_escolhe_jogada(n,m):
	jogada = int(input('Quantas peças você vai tirar? '))

	while jogada > m or jogada <= 0:
		print('Oops! Jogada inválida! Tente de novo.')
		jogada = int(input('Quantas peças você vai tirar? '))
	return jogada


def partida():
	
	print('\nVoce escolheu um isolada!\n')

	n = int(input('Quantas peças? '))
	m = int(input('Limite de peças por jogada? '))
	resto = n
	
	if n % (m + 1) == 0:
		print('\nVocê começa!')
		
		while resto > 0:
			
			resto -= usuario_escolhe_jogada(n,m)
			print('Você tirou uma peça.')
			if resto <= 0:
				print('\nVocê ganhou!\n')
				return 1					
			else:
				print('Agora restam {} peças no tabuleiro.\n'.format(resto))
				
				resto -= computador_escolhe_jogada(n,m)
				print('O computador tirou uma peça.')
				if resto <= 0:
					print('Fim do jogo! O computador ganhou!')
					return 2
	else:
		print('\nComputador começa!')
		while resto > 0:
			
			resto -= computador_escolhe_jogada(n,m)
			print('Computador tirou uma peça.')
			if resto <= 0:
				print('\nFim do jogo! O computador ganhou!\n')
				return 2					
			else:
				print('Agora restam {} peças no tabuleiro.\n'.format(resto))
				
				resto -= usuario_escolhe_jogada(n,m)
				print('\nVocê tirou uma peça.')
				if resto <= 0:
					print('Você ganhou!')
					return 1


def campeonato():
	count_jogador = 0
	count_computador = 0
	k = 1
	print('\nVoce escolheu um campeonato!\n')
	while k <= 3:
		print('**** Rodada {} ****'.format(k))
		if partida() == 1:
			count_jogador += 1
		else:
			count_computador += 1

		k += 1
	print('Placar: Você {} X {} Computador'.format(count_jogador, count_computador))


def main():
	print('Bem-vindo ao jogo do NIM! Escolha:')
	opcao = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2\n:#'))

	if opcao == 1:
		partida()
	else:
		if opcao == 2:
			campeonato()


main()
