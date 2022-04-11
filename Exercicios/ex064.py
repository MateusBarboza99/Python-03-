núm = cont = total = 0
núm = int(input('Digite um número [999 para Parar]: '))
while núm != 999:
    total += núm
    cont += 1
    núm = int(input('Digite um número [999 para Parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, total))


