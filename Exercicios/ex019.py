import random
n1 = str(input('Como se Chama o Primeiro Aluno: '))
n2 = str(input('Como se Chama o Segundo Aluno:'))
n3 = str(input('Como se Chma o Terceiro Aluno:'))
n4 = str(input('Como se Chama o Terceiro Aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))

