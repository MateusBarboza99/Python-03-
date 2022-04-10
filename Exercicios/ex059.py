from time import sleep
valor1 = int(input('Digite Primeiro valor: '))
valor2 = int(input('Digite segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qual opção você deseja ? '))
    if opção == 1:
        total = valor1 + valor2
        print('A soma entre {} + {} é igual a {}'.format(valor1, valor2, total))
    elif opção == 2:
        produto = valor1 * valor2
        print('Multiplicando {} x {} é igual a {}'.format(valor1, valor2, produto))
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
            print('O Maior número entre {} e {} foi o {}'.format(valor1, valor2, maior))
    elif opção == 4:
        print('Por favor Informe os número novamente: ')
        valor1 = int(input('Digite Primeiro valor: '))
        valor2 = int(input('Digite segundo valor: '))
    elif opção == 5:
        print('Finalizando.......')
        sleep(4)
    else:
        print('Opção Invalida! Tente Novamente!! ')
    print('=-=' * 10)
    sleep(2)
print('Fim do Programa! Volte sempre!!!')

