núm = [[], []]
valor = 0
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}ª Valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='* 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares foram {núm[0]}')
print(f'Os valores ímpares foram {núm[1]}')








