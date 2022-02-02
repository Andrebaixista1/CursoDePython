# Exercício Python 103: Faça um programa que tenha uma função 
# chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
# algum dado não tenha sido informado corretamente.
import os
os.system('cls')

# jogador = input('Nome do jogador: ')
# gols = input('Número de gols: ')

# def ficha(jogador, gols):
#     if jogador == '':
#         jogador = '<Desconhecido>'
#     if gols == '':
#         gols = 0
#     print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

# ficha(jogador, gols)

# Outra forma de fazer

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')



n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)