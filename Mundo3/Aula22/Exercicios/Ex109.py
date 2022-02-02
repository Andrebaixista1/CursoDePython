# Exercício Python 109: Modifique as funções que form criadas no 
# desafio 107 para que elas aceitem um parâmetro a mais, informando se 
# o valor retornado por elas vai ser ou não formatado pela 
# função moeda(), desenvolvida no desafio 108.

import moeda as md
import os
os.system('cls')

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {md.moeda(p,typemd=True)} é {md.moeda(md.metade(p), typemd=True)}')
# print(f'O dobro de {md.moeda(p,typemd=False)} é {md.moeda(md.dobro(p), typemd=True)}')
# print(f'Aumentando 10%, temos {md.moeda(md.aumentar(p, 10), typemd=True)}')
# print(f'Diminuindo 10%, temos {md.moeda(md.diminuir(p, 10), typemd=False)}')


# Outra forma de fazer
p = float(input('Digite o preço: R$ '))
print(f'A metade de {md.moeda(p)} é {md.metade(p, True)}')
print(f'O dobro de {md.moeda(p)} é {md.dobro(p, True)}')
print(f'Aumentando 10%, temos {md.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {md.diminuir(p, 13)}')