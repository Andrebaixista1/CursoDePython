# Exercício Python 69: Crie um programa que leia a idade e o 
# sexo de várias pessoas. A cada pessoa cadastrada, o 
# programa deverá perguntar se o usuário quer ou não 
# continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
contIdade = femIdade = cont = 0
while True:
    
    print('----- Novo Cadastro -----\n')

    idade = int(input('Digite a idade: '))
    cont += 1
    sexo = ' '
    while sexo not in 'MF': # Validador se digitou um valor válido
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] 
    
    opcao = ' '
    while opcao not in 'SN': # Validador se digitou um valor válido
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        
    

    if sexo == 'M':
        contIdade += 1 
    if sexo == 'F' and idade < 20:
        femIdade += 1
    if opcao in 'Nn':
        
        break
    

print('*=*  Relatório Criado  *=*')
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) Ao todo temos {contIdade} homens com mais de 18 anos.')
print(f'C) Ao todo temos {femIdade} mulheres com menos de 20 anos.')


