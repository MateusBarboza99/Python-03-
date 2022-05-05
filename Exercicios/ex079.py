números = list()
while True:
    n = (int(input('Digite um Número: ')))
    if n not in números:
        números.append(n)
        print('Número digitado com sucesso....')
    else:
        print('Número Duplicado! Não vai ser adicionado...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
print('=-'* 30)
números.sort()
print(f'Você digitou os números {números}')
print('{:^40}'.format('PROGRAMA ENCERRADO!'))



