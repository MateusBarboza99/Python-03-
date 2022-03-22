from datetime import date
atual = date.today().year
nasc = int(input('Digite o ANO? '))
idade = atual - nasc
print('O Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação:' '\033[31mMIRIM\033[m')
elif idade <= 14:
   print('Classificação:''\033[34mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação:''\033[32mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação:''\033[35mSÊNIOR\033[m')
elif idade > 25:
    print('Classificação:''\033[36mMASTER\033[m')



