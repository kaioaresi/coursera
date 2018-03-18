n = int(input('Digite um númeor: '))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 10) // 100

print('Milhar = {}, Centena = {}, Dezena = {}, Unidade = {}'.format(milhar, centena, dezena, unidade))

