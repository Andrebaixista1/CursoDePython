# Exercício Python 68: Faça um programa que jogue par ou 
# ímpar com o computador. O jogo só será interrompido 
# quando o jogador perder, mostrando o total de vitórias 
# consecutivas que ele conquistou no final do jogo.

# import random 
# import time

# cont = 0

# while True:
#     val = int(input('Digite um valor: '))
#     parImpar = str(input('Par ou ímpar? [P/I] ')).upper()
#     cpu = random.randint(0, 1000)

#     if parImpar == 'P':
#         if (val+cpu) % 2 == 0:
#             cont += 1
#             print('*='*20)
#             print('Deu par! Você venceu!')
#             print('*='*20)
#         else:
#             print('*='*20)
#             print('Deu impar! Você perdeu!')
#             print(f'Você venceu {cont} vezes.')
#             print('*='*20)
#             break
#     if parImpar == 'I':
#         if (val+cpu) % 2 == 0:
#             cont += 1
#             print('*='*20)            
#             print('Deu par! Você venceu!')
#             print('*='*20)
#         else:
#             print('*='*20)
#             print('Deu impar! Você perdeu!')
#             print(f'Você venceu {cont} vezes.')
#             print('*='*20)
#             break

# Outra forma de fazer:

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' \n')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
    print('Vamos jogar novamente...')
    print('Você venceu {} vezes.'.format(v))

    




        