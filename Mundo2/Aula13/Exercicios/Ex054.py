# Exercício Python 54: Crie um programa que leia o ano de nascimento 
# de sete pessoas. No final, mostre quantas pessoas ainda não 
# atingiram a maioridade e quantas já são maiores.
from datetime import date

totalMaior = 0
totalMenor = 0

for c in range(0, 7):
    ano_atual = date.today().year
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c+1)))
    ano = ano_atual - ano
    if ano >= 21:
        totalMaior += 1
    else:
        totalMenor += 1

print('\n{} pessoas são maiores de idade.'.format(totalMaior))
print('{} pessoas são menores de idade.'.format(totalMenor))





