# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e 
# a razão de uma PA, mostrando os 10 primeiros termos da progressão 
# usando a estrutura while.

print('='*30)
print('PROGRESSÃO ARITMÉTICA')
print('='*30)

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n1
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' → ')
    termo += r
    cont += 1

print('FIM')

