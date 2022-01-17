# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 == lado2 == lado3:
    print('O triângulo é EQUILÁTERO!')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é ISÓSCELES!')
else:
    print('O triângulo é ESCALENO!')