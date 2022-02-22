preço = float(input('Quanto custa esse Produto: R$'))
desc = preço - (preço * 5 / 100)
print('O Produto que custa {:.2f} \nTeve um desconto de 5% \nAgora vai custar R${:.2f} '.format(preço, desc))

