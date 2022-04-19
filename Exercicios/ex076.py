print('='* 40)
print('{:^40}'.format('Listagem de Preços!!'))
print('='* 40)
listagem = ('Espeto de Carne',  8.00,
            'Espeto de Frango',  5.00,
            'Espeto de Linguiça',  5.50,
            'Espeto de Kafta',  6.00,
            'Espeto de Queijo',  6.50,
            'Espeto de Medalhão Frango',  6.00,
            'Espeto de Mandioca C/Bacon',  6.00,
            'Espeto de Filé de Tilapia', 6.50,
            'Espeto de Coração',  6.50,
            'Espeto de Linguiça C/Pimenta', 6.50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 40)

