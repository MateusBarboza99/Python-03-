def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[31mNÃO VOTA\033[m '
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: \033[33mVOTO OPCIONAL\033[m '
    else:
        return f'Com {idade} anos: \033[32mVOTO OBRIGATÓRIO.\033[M'


#Programa principal
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
