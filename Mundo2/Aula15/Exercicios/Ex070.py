# Exercício Python 70: Crie um programa que leia o nome e o 
# preço de vários produtos. O programa deverá perguntar se 
# o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

total = maior1000 = cont = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))

    total += preco
    cont += 1
    if preco > 1000:
        maior1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = produto
    
    resp = ' '    
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')   
print(f'Temos {maior1000} custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')

