# Exercício Python 085: Crie um programa onde o usuário possa 
# digitar sete valores numéricos e cadastre-os em uma lista única que 
# mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
import os
os.system('cls')

num = [[], []]
valor = 0   

for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os valores pares são {num[0]}')
print(f'Os valores impares são {num[1]}')



    
