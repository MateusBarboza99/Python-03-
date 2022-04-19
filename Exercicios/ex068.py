print('-=-' * 10)
print('VAMOS JOGAR PAR ou IMPAR')
print('-=-'* 10)
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total} ', end='')
    print('Deu par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você vendeu! ')
            v += 1
        else:
            print('Você Perdeu! ')
            break
    elif tipo == 'I':
        print('Você Venceu! ')
        v += 1
    else:
        print('Você Perdeu! ')
        break
    print('Vamos jogar novamente ....')
print(f'Gamer Over! Você venceu {v} vezes.')







