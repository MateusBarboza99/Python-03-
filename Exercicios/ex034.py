salário = float(input('Quanto você ganha na Empresa: R$'))
if salário <= 1250:
    reajuste = salário + (salário * 15 / 100)
    print('Você ganhava R${:.2f} com Aumento você vai passar a ganhar R${:.2f} Agora'.format(salário, reajuste))
else:
    reajuste = salário + (salário * 10 / 100)
    print('Você ganhava R${:.2f} com Aumento você vai passar a ganhar R${:.2f} Agora'.format(salário, reajuste))





