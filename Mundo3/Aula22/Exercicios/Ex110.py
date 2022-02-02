# Exercício Python 110: Adicione o módulo moeda.py criado nos 
# desafios anteriores, uma função chamada resumo(), que mostre na tela 
# algumas informações geradas pelas funções que já temos no módulo criado até aqui.


import moeda as md
import os
os.system('cls')


p = float(input('Digite o preço: R$ '))
md.resumo(p, 20, 13)
print('')