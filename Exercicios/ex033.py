num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
num3 = int(input('Terceiro Valor: '))
# Verificando quen é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O Menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
