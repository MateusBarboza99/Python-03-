frase = str(input('Digite uma Frase: ')).strip().upper().strip()
print('Analisando a Frase............')
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apreceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

