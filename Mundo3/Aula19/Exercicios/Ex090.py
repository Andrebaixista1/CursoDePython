# Exercício Python 090: Faça um programa que leia nome e 
# média de um aluno, guardando também a situação em um 
# dicionário. No final, mostre o conteúdo da estrutura na tela.
import os
os.system('cls')



# fichaAluno = list()
# nome = str(input('Nome: '))
# media = float(input('Média: '))
# fichaAluno.append({'nome': nome, 'media': media})

# print('-=' * 30)

# print(f' - O nome é {fichaAluno[0]["nome"]}')
# print(f' - A média é {fichaAluno[0]["media"]}')
# if fichaAluno[0]['media'] >= 7:
#     status = 'aprovado'
# else:
#     status = 'reprovado'

# print(f' - O aluno está {status}')

# print('-=' * 30)

# Outra forma de fazer

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')






    