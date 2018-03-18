def computador_escolhe_jogada(n,m):
	if (m + 1) % n == 0: # verificando se é multiplo
		return m + 1
	else:
		return m


def usuario_escolhe_jogada(n,m):
	jogador = int(input('Quantas peças você vai tirar? '))

	if jogador > m:
		print('Oops! Jogada inválida! Tente de novo.')
		jogador = 0
		return jogador
	else:
		return jogador


def camponato(jogador, computador):
	print('**** Final do campeonato! ****')
	print('Placar: Você {} X {} Computador'.format(jogador, computador))

def partida():

	print('Bem-vindo ao jogo do NIM! Escolha:\n')

	opcao = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n$:'))
	
	if opcao == 1:
		print('Voce escolheu uma partida isolada!\n')
		print('**** Rodada Unica ****\nVamos começar!')
		
		n = int(input('Quantas peças? '))
		m = int(input('Limite de peças por jogada? '))
		
		resta = n

		if n % m == 0:
			print('\nComputador começa!\n')
			
			while resta != 0:
				print('O computador tirou uma peça.')
				resta -= computador_escolhe_jogada(n,m)
				
				if resta == 0:
					print('Fim do jogo! O computador ganhou!\n')
					break
				else:
					print('Agora restam {} peças no tabuleiro.\n'.format(resta))
				
				resta -= usuario_escolhe_jogada(n,m)
				
				print('Você tirou uma peça.')

				if resta == 0:
					print('Fim do jogo! O você ganhou!\n')
					break
				else:
					print('Agora restam {} peças no tabuleiro.\n'.format(resta))
		else:
			print('\nVocê começa!\n')

			while resta != 0:
				
				resta -= usuario_escolhe_jogada(n,m)
				print('Você tirou uma peça.')

				if resta == 0:
					print('Fim do jogo! O você ganhou!\n')
					break
				else:
					print('Agora restam {} peças no tabuleiro.\n'.format(resta))

				print('O computador tirou uma peça.')
				resta -= computador_escolhe_jogada(n,m)
				
				if resta == 0:
					print('Fim do jogo! O computador ganhou!\n')
					break
				else:
					print('Agora restam {} peças no tabuleiro.\n'.format(resta))
	else:
		if opcao == 2:
			print('Voce escolheu um campeonato!')
			k = 1
			count_jogador = 0
			count_computador = 0

			while k <= 3:
				print('**** Rodada {} ****'.format(k))
				k += 1

				n = int(input('Quantas peças? '))
				m = int(input('Limite de peças por jogada? '))
				
				resta = n

				if n % m == 0:
					print('\nComputador começa!\n')
					
					while resta != 0:
						print('O computador tirou uma peça.')
						resta -= computador_escolhe_jogada(n,m)
						
						if resta == 0:
							print('Fim do jogo! O computador ganhou!\n')
							count_computador += 1
							break
						else:
							print('Agora restam {} peças no tabuleiro.\n'.format(resta))
						
						resta -= usuario_escolhe_jogada(n,m)
						
						print('Você tirou uma peça.')

						if resta == 0:
							print('Fim do jogo! O você ganhou!\n')
							count_jogador += 1
							break
						else:
							print('Agora restam {} peças no tabuleiro.\n'.format(resta))
				else:
					print('\nVocê começa!\n')

					while resta != 0:
						
						resta -= usuario_escolhe_jogada(n,m)
						print('Você tirou uma peça.')

						if resta == 0:
							print('Fim do jogo! O você ganhou!\n')
							count_jogador += 1
							break
						else:
							print('Agora restam {} peças no tabuleiro.\n'.format(resta))

						print('O computador tirou uma peça.')
						resta -= computador_escolhe_jogada(n,m)
						
						if resta == 0:
							print('Fim do jogo! O computador ganhou!\n')
							count_computador += 1
							break
						else:
							print('Agora restam {} peças no tabuleiro.\n'.format(resta))

	camponato(count_jogador, count_computador)

partida()