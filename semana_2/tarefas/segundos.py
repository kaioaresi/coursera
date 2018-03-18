
tempo = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = tempo // 86400
hora = (tempo // 3600) % 24
segundos = (tempo % 86400) % 3600
minuto = segundos // 60
segundos_f = segundos % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dia, hora, minuto, segundos_f))