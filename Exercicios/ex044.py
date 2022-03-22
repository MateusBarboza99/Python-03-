print('{:=^40}'.format('LOJAS MATEUS'))
preço = float(input('Qual Valor da sua Compra: R$'))
print('''\033[31mFORMAS DE PAGAMENTO\033[m:
[ 1 ] Á vista Dinheiro/ Cheque
[ 2 ] Á vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opção = int(input('\033[34mQual é a Opção\033[m? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} ' '\033[34mSEM JUROS\033[m'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('\033[34mQuantas parcelas\033[m? '))
    parcela = total / totparc
    print('Sua Comprar será parcelada em {}x de R${:.2f} ' '\033[31mCOM JUROS\033[m'.format(totparc, parcela))
else:
    total = preço
    print('\033[31mOPÇÃO INVÁLIDA\033[m' 'de Pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2F} no final.'.format(preço, total))



