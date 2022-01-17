# Estruturas de repetição FOR

# Contando ao contrario
# for c in range(10, 0, -1):
#     print(c)
# print('Fim')

# inicio = int(input('Inicio: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))

# for c in range(inicio, fim+1, passo):
#     print(c)
# print('Fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
