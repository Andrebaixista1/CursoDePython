# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que 
# vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime
import os

# os.system('cls')
# def voto(ano):
#     if idade < 16:
#         print(f'Com {idade} anos o voto não é obrigatório.')
#     elif idade < 18 or idade > 65:
#         print(f'Com {idade} anos o voto é opcional.')
#     else:
#         print(f'Com {idade} anos o voto é obrigatório.')

# print('-='*20)
# ano = int(input('Digite o ano de nascimento: '))
# idade = datetime.now().year - ano
# voto(ano)

    
# Outra forma de fazer

os.system('cls')
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos o voto não é obrigatório.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional.'
    else:
        return f'Com {idade} anos o voto é obrigatório.'
print(voto(2000))
