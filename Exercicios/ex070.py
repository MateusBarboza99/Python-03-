print('='* 40)
print('{:^40}'.format('LOJA DO  MATEUZINHOO!!!'))
print('='* 40)
total = totmil= menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Qual o valor: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('PROGRAMA ENCERRADO!!!'))
print(f'Valor total da sua compra foi de R${total:.2f}')
print(f'Temos {totmil} produto custando mais de R$ 1000.00 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


