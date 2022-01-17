# Exercício Python 56: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. No final do programa, mostre: a média de 
# idade do grupo, qual é o nome do homem mais velho e quantas 
# mulheres têm menos de 20 anos.

# somaidade = 0

# for c in range(1,5):
#     nome = str(input('Digite o nome: '))
#     idade = int(input('Digite a idade: '))
#     sexo = str(input('Digite o sexo [M/F]: ')).upper()
#     somaidade += idade / 2
#     if c == 1 and sexo == 'F':
#         maisvelho = nome
#         velho = idade
#     if sexo == 'F' and idade > velho:
#         maisvelho = nome
#         velho = idade


# print('A mais velha é {} com {} anos.'.format(maisvelho, velho))
# print('A média de idade do grupo é {}'.format(somaidade))

# ================================================================
# Outra forma de fazer
somaidade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1



mediaIdade = somaidade / 4
print('A média de idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
    