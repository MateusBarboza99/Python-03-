real = float(input('Quanto você tem na Carteira? R$'))
dolar = real / 5.11
euro = real / 5.76
print('Com R${:.2f}  você pode comprar U$${:.2f} e €{:.2f} '.format(real, dolar, euro))




