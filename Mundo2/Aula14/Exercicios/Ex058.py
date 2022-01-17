# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o 
# computador vai “pensar” em um número entre 0 e 10. Só que agora o 
# jogador vai tentar adivinhar até acertar, mostrando no final quantos 
# palpites foram necessários para vencer.

import random
from time import sleep

computador = random.randint(0, 10)
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
num = 0
tentativas = 0
# while num != computador:
#     num = int(input('Será que você consegue adivinhar qual foi?'))
#     if num > computador:
#         print('Menos...')
#     if num < computador:
#         print('Mais...')
#     if num == computador:
#         print('Parabéns! Você acertou!')
#     tentativas += 1

# print('Você precisou de {} tentativas.'.format(tentativas))

# # Outra forma de fazer:

acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Hum você disse {}'.format(jogador))
            print('É mais...')
        else:
            print('Hum você disse {}'.format(jogador))
            print('É menos...')

    tentativas += 1
print('O número que pensei foi {}.'.format(computador))
print('Acertou com {} tentativas!'.format(tentativas))

