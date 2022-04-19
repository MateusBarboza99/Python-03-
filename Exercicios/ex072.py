cont = ('zero', 'um','dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
          'onze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um valor de [0 até 20]: '))
    if 0 <= núm <= 20:
        break
    print('Féra tente novamente.', end='')
print(f'Você digitou o número {cont[núm]}')


