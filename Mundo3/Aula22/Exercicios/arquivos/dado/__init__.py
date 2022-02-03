from Mundo3.Aula22.Exercicios.arquivos import moeda

def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco*taxa/100)
    return res if format is False else moeda(res)

def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco*taxa/100)
    return res if format is False else moeda(res)

def dobro(preco=0, format=False):
    res = preco * 2
    return res if not format else moeda(res)

def metade(preco=0, format=False):
    res = preco /2
    return res if not format else moeda(res)


def resumo(preco=0, mais=10, menos=5):
    titulo = ('Resumo do Valor')
    tam = len(titulo) + 35
    print(f'-' * tam)
    print(f'{titulo:^50}')
    print(f'-' * tam)

    # Dados = ('Preço analisado: ', moeda(preco),
    #          'Dobro de Preço: ', dobro(preco, True),
    #          'Metade do Preço: ', metade(preco, True),
    #          f'{mais}% de aumento:', moeda(aumentar(mais,True)),
    #          f'{menos}% de redução: ', moeda(diminuir(menos, True)))

    # for pos in range(0, len(Dados)):
    #     if pos % 2 == 0:
    #         print(f'{Dados[pos]:<35}', end='')
    #     else:
    #         print(f'{Dados[pos]}')

    # Outra forma de fazer
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro de Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{mais}% de aumento: \t{moeda(aumentar(mais, True))}')
    print(f'{menos}% de redução: \t{moeda(diminuir(menos, True))}')