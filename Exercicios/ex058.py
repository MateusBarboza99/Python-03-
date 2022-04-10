from random import randint
computador = randint(0, 10)
print('Sou seu Computador...Acabei de pensar em um número entre 0 e 10 ')
print('Qual você acha que foi Paçoca? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Bora Lahhh tem um Palpite???'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Quase...Um pouco MAIS, tente mais uma Vez: ')
        elif jogador > computador:
            print('Passo perto...Um pouco MENOS, Tente mais uma Vez: ')
print('Paçoca você Acertou com {} tentativas, PARABENS!'.format(palpites))
