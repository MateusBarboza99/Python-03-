def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaaumento=10, taxaredução=5):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço,True)}')
    print(f'Metade do Preço: \t{metade(preço,True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preço,taxaaumento, True)}')
    print(f'{taxaredução}% redução: \t\t{diminuir(preço,taxaredução,True)}')
    print('-' * 30)



