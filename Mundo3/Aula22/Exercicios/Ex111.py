# Exercício Python 111: Crie um pacote chamado utilidadesCeV que 
# tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o 
# primeiro pacote e mantenha tudo funcionando.

from Mundo3.Aula22.Exercicios.arquivos import moeda as md
from arquivos import dado as dd


import os
os.system('cls')


p = float(input('Digite o preço: R$ '))
md.resumo(p, 20, 13)
print('')