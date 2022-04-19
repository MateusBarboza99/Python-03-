from math import frexp
núm = (int(input('Digite um valor: ')),
      int(input('Outro número: ')),
      int(input('Mais um número: ')),
      int(input('O último número:')))
print(f'Os valores Digitados foi {núm}')
print(f'O valor 9 foi Digitado {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O número 3 apareceu na {núm.index(3)+1}ª posição. ')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
