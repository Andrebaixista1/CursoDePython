# Exercício Python 103: Faça um programa que tenha uma função 
# chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
# algum dado não tenha sido informado corretamente.
import os
os.system('cls')

jogador = input('Nome do jogador: ')
gols = input('Número de gols: ')

def ficha(jogador, gols):
    if jogador == '':
        jogador = '<Desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

ficha(jogador, gols)