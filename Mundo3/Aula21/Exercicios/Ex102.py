# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será 
# um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep
import os
os.system('cls')

def fatorial(val, show):
    """
    -> Calcula o fatorial de um número.
    :param val: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número.

    """
    if show == True:
        c = val
        i = 1
        while c > 0:
            print(f'{c}', end='', flush=True)
            i *= c
            c -= 1
            sleep(0.3)
            print(' x ' if c > 0 else ' = ', end='', flush=True)
        print(f'{i}')
    else:
        c = val
        i = 1
        while c > 0:
            i *= c
            c -= 1
            sleep(0.3)
        print(f'{i}')

fatorial(5, True)
help(fatorial)


