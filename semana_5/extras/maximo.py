#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
#n3 = int(input('Digite mais um valor: '))


def maximo(n1,n2,n3):

	if n1 > n2 and n1 > n3:
		return n1
	elif n1 < n2 and n2 > n3:
		return n2
	else:
		return n3

#print(maximo(n1,n2,n3))