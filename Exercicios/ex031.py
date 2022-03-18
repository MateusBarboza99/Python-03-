distância = int(input('Qual é a Distância da Viagem? '))
print('Você está prestes a começar uma viagem de {}km. '.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço de sua passagem serâ de R${:.2f} '.format(preço))

