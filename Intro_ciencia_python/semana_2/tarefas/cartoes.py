
nome = input('Digite o nome do cliente: ')
dia = input('Digite o dia de vencimento: ')
mes = input('Digite o mês de vencimento: ')
valor = float(input('Digite o valor da fatura: '))

print('Olá, {}'.format(nome, dia, mes))
print('A sua fatura com vencimento em {} de {} no valor de R$ {},00 está fechada.'.format(dia, mes, valor))
