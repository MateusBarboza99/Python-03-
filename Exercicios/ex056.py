somaidade = 0
médiaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1, 5):
    print('------{}ª PESSOA-------'.format(pess))
    nome = str(input('Nome: '.format(pess))).strip()
    idade = int(input('Idade: '.format(pess)))
    sexo = str(input('[M/F]: '.format(pess))).strip()
    somaidade += idade
    if pess == 1 and sexo in 'Mm':
        maoiridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maoiridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é {} anos'.format(médiaidade))
print('O Homem mais velho do Grupo tem {} anos e se chama {}'.format(maoiridadehomem, nomevelho))
print('No grupo tem {} mulheres com menos de 20 anos'.format(totmulher20))


