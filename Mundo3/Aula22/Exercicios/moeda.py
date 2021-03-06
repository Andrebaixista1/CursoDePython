# def metade(v):
#     v = v /2
#     return v

# def dobro(v):
#     v = v *2
#     return v

# def aumento(v):
#     v = v + (v *10 /100)
#     return v

# def diminuir(v):
    # v = v - (v*10/100)
    # return v

# Outra forma de fazer

# def aumentar(preco=0, taxa=0):
#     res = preco + (preco*taxa/100)
#     return res

# def diminuir(preco=0, taxa=0):
#     res = preco - (preco*taxa/100)
#     return res

# def dobro(preco=0):
#     res = preco * 2
#     return res

# def metade(preco=0):
#     res = preco /2
#     return res
# # Ex108
# def moeda(preco=0, moeda='R$ '):
#     return f'{moeda}{preco:>.2f}'.replace('.',',')

# # Ex109
# # def moeda(preco=0, moeda='R$ ', typemd=False):
# #     if typemd:
# #         return f'{moeda}{preco:>.2f}'.replace('.',',')
# #     else:
# #         return f'{preco}'
# # Outra forma de fazer
# def aumentar(preco=0, taxa=0, format=False):
    
#     res = preco + (preco*taxa/100)
#     return res if format is False else moeda(res)

# def diminuir(preco=0, taxa=0, format=False):
#     res = preco - (preco*taxa/100)
#     return res if format is False else moeda(res)

# def dobro(preco=0, format=False):
#     res = preco * 2
#     return res if not format else moeda(res)

# def metade(preco=0, format=False):
#     res = preco /2
#     return res if not format else moeda(res)

# def moeda(preco=0, moeda='R$ ', typemd=False):
#     return f'{moeda}{preco:>.2f}'.replace('.',',')
    
# Ex110
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

def moeda(preco=0, moeda='R$ ', typemd=False):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
    
def resumo(preco=0, mais=10, menos=5):
    titulo = ('Resumo do Valor')
    tam = len(titulo) + 35
    print(f'-'*tam)
    print(f'{ titulo:^50}')
    print(f'-'*tam)

    # Dados = ('Pre??o analisado: ', moeda(preco),
    #          'Dobro de Pre??o: ', dobro(preco, True),
    #          'Metade do Pre??o: ', metade(preco, True),
    #          f'{mais}% de aumento:', moeda(aumentar(mais,True)),
    #          f'{menos}% de redu????o: ', moeda(diminuir(menos, True)))
    
    # for pos in range(0, len(Dados)):
    #     if pos % 2 == 0:
    #         print(f'{Dados[pos]:<35}', end='')
    #     else:
    #         print(f'{Dados[pos]}')


    # Outra forma de fazer
    print(f'Pre??o analisado: \t{moeda(preco)}')
    print(f'Dobro de Pre??o: \t{dobro(preco, True)}')
    print(f'Metade do Pre??o: \t{metade(preco, True)}')
    print(f'{mais}% de aumento: \t{moeda(aumentar(mais,True))}')
    print(f'{menos}% de redu????o: \t{moeda(diminuir(menos, True))}')
    # print(Dados)


def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO! "{entrada}" ?? um pre??o inv??lido!\033[m')
        else:
            valido = True
            return float(entrada.replace(',','.'))



