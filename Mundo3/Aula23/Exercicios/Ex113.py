# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from cgi import print_form
import os
import functionsCeV as cev
os.system('cls')

num = cev.LeiaInt('Digite um valor inteiro: ')
num2 = cev.LeiaFloat('Digite um real: ')
print(f'O valor digitado foi {num} e {num2}')
