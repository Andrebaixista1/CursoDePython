# Exercício Python 108: Adapte o código do desafio #107, criando uma 
# função adicional chamada moeda() que consiga mostrar os números como um 
# valor monetário formatado.

import moeda as md
import os
os.system('cls')

p = float(input('Digite o preço: R$ '))
print(f'A metade de {md.moeda(p)} é {md.moeda(md.metade(p))}')
print(f'O dobro de {md.moeda(p)} é {md.moeda(md.dobro(p))}')
print(f'Aumentando 10%, temos {md.moeda(md.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {md.moeda(md.diminuir(p, 10))}')