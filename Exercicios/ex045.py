from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''\033[1;31mSuas opções\033[m:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\033[1;34mQual é a sua Jogada?\033[m '))
print('\033[1;30mJO\033[m')
sleep(1)
print('\033[1;34mKEN\033[m')
sleep(1)
print('\033[1;33mPO!!\033[m')
sleep(1)
print('\033[35m-=\033[m' * 11)
print('\033[1;32mComputador jogou\033[m '  ' \033[1;35m{}\033[m'.format(itens[computador]))
print('\033[1;36mJogador jogou\033[m ' ' \033[1;32m{}\033[m'. format(itens[jogador]))
print('\033[35m-=\033[m' * 11)
if computador == 0:# computador jogou PEDRA
    if jogador == 0:
        print('\033[1;37mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;43mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[4;33;40mJOGADA INVÁLIDA\033[m!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1;37mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;34mJOGADOR VENCEU\033[m')
    else:
        print('\033[4;33;;40mJOGADA INVÁLIDA\033[m!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[1;34mJOGADOR VENCEU\033[m')
    elif jogador == 1:
          print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
          print('\033[1;37mEMPATE\033[m')
    else:
        print('\033[4;33;mJOGADA INVÁLIDA\033[m!')





