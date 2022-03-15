nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome........')
print('Seu nome em Maiúscula é {}'.format(nome.upper()))
print('Seu nome em Minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} Letras'.format(len(nome) - nome.count(' ')))
#print('Seu Primeiro tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


 


















