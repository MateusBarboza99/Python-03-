lista = []
for cont in range(0, 5):
    núm = (int(input('Digite um valor : ')))
    if cont == 0 or núm > lista[-1]:
        lista.append(núm)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if núm <= lista[pos]:
                lista.insert(pos, núm)
                print(f'Valor adiconado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os Valores digitados foram colocados em ordem {lista}')


