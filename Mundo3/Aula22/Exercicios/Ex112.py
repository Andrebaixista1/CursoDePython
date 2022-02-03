# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um 
# módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como 
# a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
import moeda as md
import os
os.system('cls')


p = md.leia_dinheiro('Digite o preço: R$ ')
md.resumo(p, 20, 13)
print('')