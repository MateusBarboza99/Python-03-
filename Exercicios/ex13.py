salário = float(input('Quanto você ganha na Empresa: R$'))
reajuste = salário + (salário * 15 / 100)
print('Seu salário é de R${:.2f} com reajuste de 15%, você passa a ganhar R${:.2f}'.format(salário, reajuste))
