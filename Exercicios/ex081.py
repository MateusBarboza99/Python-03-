valores = list()

while True:
    valores.append(int(input('Digite o Valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram Digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'A lista de Valores, colocado na ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!!')
else:
    print('O valor 5 não faz parte da lista!!')


