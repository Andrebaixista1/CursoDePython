# Maior e menor valor digitado

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))