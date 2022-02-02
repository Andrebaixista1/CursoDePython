# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e 
# tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import os
from time import sleep
from random import randint
from operator import itemgetter

os.system('cls')

jogo = {
    'Jogador 1' : randint(1, 6),
    'Jogador 2' : randint(1, 6),
    'Jogador 3' : randint(1, 6),
    'Jogador 4' : randint(1, 6)
}
ranking = dict()
print('Valores sorteados:')
for k, j in jogo.items():
    print(f'{k} tirou {j}')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar -> {v[0]} com {v[1]}')
    sleep(0.5)

