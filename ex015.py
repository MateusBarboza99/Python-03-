dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km Rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O Aluguel a pagar é de R${:.2f}'.format(pago))


