# Exercício Python 51: Desenvolva um programa que leia o primeiro 
# termo e a razão de uma PA. No final, mostre os 10 primeiros termos 
# dessa progressão.

print('='*30)
print('PROGRESSÃO ARITMÉTICA')
print('='*30)

termoUm = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = termoUm + (10 - 1) * razao

for c in range(termoUm, décimo + razao, razao):
    print('{}'.format(termoUm), end=' → ')
    termoUm += razao

print('FIM')