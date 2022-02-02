# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que 
# receba as dimensões de um terreno retangular (largura e comprimento) e mostre a 
# área do terreno.

print('Controle de Terrenos')
print('-'*20)


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

def area(largura, comprimento):
    
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


area(largura, comprimento)
