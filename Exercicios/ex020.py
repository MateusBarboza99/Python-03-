from random import shuffle
n1 = str(input('Como se Chama o Primeiro Aluno: '))
n2 = str(input('Como se Chama o Segundo Aluno:'))
n3 = str(input('Como se Chma o Terceiro Aluno:'))
n4 = str(input('Como se Chama o Terceiro Aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A Ordem de Apresentação será ')
print(lista)
