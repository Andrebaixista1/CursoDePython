import os
os.system('cls')

# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

cont = 0
lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
    

    
print('*='*30)
print(f'Foram digitados {cont} números.')
#  Outra forma de fazer:
print(f'Você digitou {len(lista)} números.')
print('*='*30)

print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')

