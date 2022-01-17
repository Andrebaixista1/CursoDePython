# Exercício Python 45: Crie um programa que faça o computador 
# jogar Jokenpô com você.

import random
from time import sleep

print('-=' * 20)
print('Jokenpô')
print('-=' * 20)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista = ('PEDRA', 'PAPEL', 'TESOURA')
escolha = int(input('Qual é a sua escolha? '))

print('-=' * 20)
print('Computador jogando...')
print('-=' * 20)
computador = random.randint(0, 2)
sleep(3)
if escolha == computador:
    print('Você escolheu {} e o computador escolheu {}'.format(lista[escolha], lista[computador]))
    print('EMPATE!')
elif escolha < computador:
    print('Você escolheu {} e o computador escolheu {}'.format(lista[escolha], lista[computador]))
    print('Você perdeu!')
elif escolha > computador:
    print('Você escolheu {} e o computador escolheu {}'.format(lista[escolha], lista[computador]))
    print('Você ganhou!')
   





