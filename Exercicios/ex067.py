while True:
    núm = int(input('Digite um Número para ver a Tabúada: '))
    print('-' * 30)
    if núm < 0:
        break
    for c in range(1, 11):
        print(f'{núm} x {c}= {núm*c}')
    print('-' * 30)
print('TABUADA ENCERRADA!!!')



