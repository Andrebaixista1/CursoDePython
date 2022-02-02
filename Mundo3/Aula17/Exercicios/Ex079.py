import os
os.system('cls')

# Exercício Python 079: Crie um programa onde o 
# usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele 
# não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor)
        print(f'Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! Não será adicionado.')
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break


print(f'Os valores digitados foram {sorted(lista)}')

# Outra forma de fazer

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
           
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break

print(f'Você digitou os valores {numeros}')

    

