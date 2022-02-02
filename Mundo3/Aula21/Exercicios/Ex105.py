# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# – A maior nota
# – A menor nota
# - A média da turma
# – A situação (opcional)




def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param retun: dicionário com várias informações sobre a turma."""
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    media = sum(n) / len(n)
    r['Média'] = f'{media:.2f}'
    if sit:
        if media >= 7:
            r['Situação'] = 'BOA'
        elif media >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'


    return r



resp = []
resp = notas(5.5, 2.5, 5.5, sit=True)
# print(resp)
help(notas)

