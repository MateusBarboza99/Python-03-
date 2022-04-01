num = int(input('Digite um Número para ver a Tabúada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
