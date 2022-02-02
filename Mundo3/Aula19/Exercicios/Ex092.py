# Exercício Python 092: Crie um programa que leia nome, ano de 
# nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário 
# receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import os
from datetime import datetime
os.system('cls')

ficha = dict()

ficha['nome'] = str(input('Nome: '))
ficha['nascimento'] = datetime.now().year - int(input('Ano de Nascimento: '))

ficha['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['carteira'] != 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salário'] = float(input('Salário: '))
    # ficha['aposentadoria'] = ficha['idade'] + (ficha['contratação'] + 35) - datetime.now().year

print('-=' * 30)
for k, v in ficha.items():
    print(f'  - {k} é igual a {v}')



