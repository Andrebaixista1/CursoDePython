from ast import While
from mailbox import NotEmptyError
import os
from tokenize import PseudoExtras
os.system('cls')

# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]


    princ.append(temp[:])
    temp.clear()



    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break

print('-='*30)
print(f'Os dados cadastrados foram {princ}')
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print('[{}]'.format(p[0]), end='')
print()
print(f'O maior peso foi {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print('[{}]'.format(p[0]), end='')
print()




