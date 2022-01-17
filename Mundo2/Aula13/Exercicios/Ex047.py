# Exercício Python 47: Crie um programa que mostre na tela todos os 
# números pares que estão no intervalo entre 1 e 50.
from time import sleep
for i in range(2, 51, 2):
    if i % 2 == 0:
        print(i)
        sleep(1)