# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que 
# vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

import os
os.system('cls')

# def LeiaInt(n):
#     n = input('Digite um número: ')
#     while n.isnumeric() == False:
#         print('\033[31mERRO! Digite um número inteiro válido.\033[m')
#         n = input('Digite um número: ')
        
#     return int(n)

# num = LeiaInt('Digite um número: ')
# print(f'Você digitou o número {num}')

# Outra forma de fazer

def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;33mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = LeiaInt('Digite um número: ')
print(f'Você digitou o número {n}')