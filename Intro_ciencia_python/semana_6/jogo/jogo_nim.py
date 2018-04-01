def computador_escolhe_jogada(n, m):
    computador = 1

    while computador != m:
        if (n - computador ) % ( m + 1 ) == 0:
            return computador
        else:
            computador += 1
    return computador


def usuario_escolhe_jogada(n, m):
    usuario = 0
    while usuario == 0:
        usuario = int(input("Quantas peças você vai tirar? "))
        if usuario > n or usuario < 1 or usuario > m:
            print("Oops! Jogada inválida! Tente de novo.")
            usuario = 0
    return usuario

def partida():
	n=int(input("Quantas peças? "))
	m=int(input("Limite de peças por jogada? "))

	if not n % ( m + 1 ) == 0 or n <= m:
		print("\nomputador começa!\n")
		
		while n > 0:
			n -= computador_escolhe_jogada(n, m)
			if n <= 0:
				print("Fim do jogo! O computador ganhou!")
				break
			print("Agora restam", n, "peças no tabuleiro.\n")
			n -= usuario_escolhe_jogada(n, m)
			if n <= 0:
				print("Fim do jogo! Você ganhou!")				
				break
			print("Agora restam", n, "peças no tabuleiro.\n")		
	else:
		print("Você começa!")	
		while n > 0:
			n -= usuario_escolhe_jogada(n, m)
			if n <= 0:
				print("Fim do jogo! Você ganhou!")
				break				
			print("Agora restam", n, "peças no tabuleiro.\n")
				
			n -= computador_escolhe_jogada(n, m)
			if n <= 0:
				print("Fim do jogo! O computador ganhou!")
				break			
			print("Agora restam", n, "peças no tabuleiro.\n")
			

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
		else:
			print('Opção invalida')


main()