# Exercício Python 078: Faça um programa que leia 5 valores 
# numéricos e guarde-os em uma lista. No final, mostre 
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

import os
os.system('cls')

lista=[]

maior = menor = 0

for v in range(0,5):
    lista.append(int(input('Digite um valor na posição {}: '.format(v))))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end='')




