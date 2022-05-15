números = []
pares = []
ímpares = []
while True:
    números.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A primeira lista completa  é {números}')
print(f'A segunda lista de números pares é {pares}')
print(f'A terceira lista de números ímpares é {ímpares}')






