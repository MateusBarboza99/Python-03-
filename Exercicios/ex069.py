tot18 = totH = totM20 = 0
while True:
    print('='* 40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('='* 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    print('=' * 40)
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O Total de pessoas com mais de 18 anos foi de:{tot18}')
print(f'A o todo temos {totH} homem cadastrado.')
print(f'E temos {totM20} Mulher com menos de 20 anos')


