from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou Pensar em Um Número Entre 0 e 5. Tente Adivinhar Paçoca...')
print('-=-' * 20)
jogador = int(input('Em que Número eu Pensei? ')) # Jogador tenta Adivinhar
print('PROCESSANDO........')
sleep(3)
if jogador == computador:
    print('PARABÊNS! Você conseguiu me Vencer Paçoca')
else:
    print('GANHEI! Eu Pensei no Número {} e não no {}!'.format(computador, jogador))
