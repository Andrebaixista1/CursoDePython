# Exercício Python 67: Faça um programa que mostre a 
# tabuada de vários números, um de cada vez, para cada 
# valor digitado pelo usuário. O programa será interrompido 
# quando o número solicitado for negativo.

# num = int(input('Quero ver a tabuada de: '))
# while num >= 0:
#     # print(f'Tabuada de {num}')
#     for i in range(1,11):
#         print(f'{num} x {i} = {num * i}')
#     num = int(input('Quero ver a tabuada de: '))
# print('Fim')

# Outra forma de fazer:
n = 0
while True:
    n - int(input('Quero ver a tabuada de: '))
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
    if n < 0:
        break
print('Programa de tabuada encerrado.')
