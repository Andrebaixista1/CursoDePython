import os
os.system('cls')

# Exercício Python 082: Crie um programa que vai ler vários números e 
# colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []


while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
   
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'A lista completa é {sorted(lista)}')
print(f'A lista de pares é {sorted(par)}')
print(f'A lista de ímpares é {sorted(impar)}')

    