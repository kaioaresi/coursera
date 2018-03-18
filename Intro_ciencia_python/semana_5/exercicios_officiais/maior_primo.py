#n = int(input('Digite um número: '))

def eprimo(numero):
    if (numero == 2):
        return True
    elif (numero % 2 == 0):
        return False
    else:
        k = 3
        while (k <= (numero / k)):
            if ((numero % k) == 0):
                return False
            k += 2
        return True
 
    return False
 
def maior_primo(numero):
 
    if (numero < 2):
        return 0
    elif (numero == 2):
        return 2
    else:
         
        while (numero > 2):
            if (eprimo(numero)):
                return numero
            numero -= 1
        return numero
 
    return 0

#print(maior_primo(n))

