n = int(input('Digite o valor de n: '))
k = n
fatorial = 1

while k > 0:
	
	fatorial *= k
	k -= 1

print(fatorial)