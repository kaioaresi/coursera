# dado sum número grande, você de somar todos os digitos do númer
'''
ex:
	12345
	1 + 2 + 3 + 4 + 5 = 15
'''

n = int(input('Digite um número qualquer: '))

unidade = n % 10 
dezena = ( n // 10) % 10
centena = (n // 100 ) % 10
milhar = (n // 10) // 100

print('Milhar = {}, Centena = {}, Dezana = {}, Unidade = {}'.format(milhar, centena, dezena, unidade))

soma = milhar + centena + dezena + unidade

print('A soma do número é {}'.format(soma))

