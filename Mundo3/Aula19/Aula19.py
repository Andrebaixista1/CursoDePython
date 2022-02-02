# Aula 19 - Dicionarios
import os
from xml.etree.ElementTree import TreeBuilder
os.system('cls')
# Tuplas ()
# Listas []
# Dicionarios {}

# dados = dict()
# or
# dados = {'nome': 'Pedro', 'idade': 22}

# dados['sexo'] = 'M'
# del dados['idade']

# filme = {
#     'titulo': 'Star Wars',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }

# print(filme.values()) # Retorna os valores
# print(filme.keys()) # Retorna as chaves
# print(filme.items()) # Retorna os pares chave/valor

# for k, v in filme.items():
#     print(f'O {k} é {v}')


 # ---------------- Exemplo 1 ----------------
# pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 22}
# # pessoas['nome'] = 'Leandro'


# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k, v in pessoas.items():
#     print(f'{k} = {v}')


# ---------------- Exemplo 2 ----------------
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])

# ---------------- Exemplo 3 ----------------


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) 
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()




