x = int(input('Digite um número: '))

check1 = x % 3
check2 = x % 5



if check1 == 0 and check2 == 0:
	print('FizzBuzz')
else:
	print(x)

