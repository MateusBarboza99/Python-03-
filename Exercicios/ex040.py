nota1 = float(input('Qual é sua Primeira Nota? '))
nota2 = float(input('Qual é sua Segunda Nota? '))
média = (nota1 + nota2) / 2
print('Tirando entre {:.1f} e {:.1f} a média do Aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em \033[31mRECUPERAÇÃO.\033[m')
elif média < 5:
    print('O aluno está \033[31mREPROVADO.\033[m')
elif média >= 7:
    print('O aluno está \033[34mAPROVADO.\033[m')



