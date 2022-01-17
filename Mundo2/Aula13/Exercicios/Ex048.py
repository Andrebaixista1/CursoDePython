# Exercício Python 48: Faça um programa que calcule a soma entre
# todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

from time import sleep
soma = 0
for i in range(1, 501, 2):
        if i % 3 == 0:
            soma = soma + i 
            sleep(0.2)
            
print('A soma dos números múltiplos de 3 é {}'.format(soma))
