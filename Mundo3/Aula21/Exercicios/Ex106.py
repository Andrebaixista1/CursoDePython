# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.
import os
os.system('cls')

c = ('\033[1;31m', '\033[1;33m', '\033[1;32m')

def ajuda(com):
    titulo
    help(com)

def titulo(msg, cor = 1):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print(f'~' * tam)    
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end = '')

comando = ''


while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!')	











    