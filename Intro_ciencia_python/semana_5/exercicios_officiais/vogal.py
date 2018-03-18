letra = input('Digite uma letra: ')

def vogal(letra):
	
	l = letra.lower()

	if l in ('a','e','i','o','u'):
		return True
	else:
		return False

print(vogal(letra))