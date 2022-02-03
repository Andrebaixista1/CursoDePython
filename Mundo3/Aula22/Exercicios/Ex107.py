# Exercício Python 107: Crie um módulo chamado moeda.py 
# que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from Mundo3.Aula22.Exercicios.arquivos import moeda as md
import os
os.system('cls')


# valor = float(input('Digite um valor: R$'))
# # aumentar()
# # diminuir()
# # dobro()

# mValor = md.metade(valor)
# dValor = md.dobro(valor)
# pValor = md.aumento(valor)
# print(f'Metade de R${valor} é R${mValor}')
# print(f'O dobre de R${valor} é R${dValor}')
# print(f'Aumentando 10%, temos R${pValor}')


# Outra forma de fazer
p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${md.metade(p)}')
print(f'O dobro de R${p} é R${md.dobro(p)}')
print(f'Aumentando 10%, temos R${md.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${md.diminuir(p, 10)}')