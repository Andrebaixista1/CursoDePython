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

# Ex109
# def moeda(preco=0, moeda='R$ ', typemd=False):
#     if typemd:
#         return f'{moeda}{preco:>.2f}'.replace('.',',')
#     else:
#         return f'{preco}'
# Outra forma de fazer
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
    