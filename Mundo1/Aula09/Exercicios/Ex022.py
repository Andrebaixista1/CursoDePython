# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nomeCompleto = input('Digite seu nome completo: ')
nomeUpper = nomeCompleto.upper()
nomeLower = nomeCompleto.lower()
nomeCompletoLen = len(nomeCompleto)
nomePrimeiro = len(nomeCompleto.split()[0])

print('Seu nome completo é: {}'.format(nomeCompleto))
print('Seu nome completo em letras maiúsculas é: {}'.format(nomeUpper))
print('Seu nome completo em letras minúsculas é: {}'.format(nomeLower))
print('Seu nome completo tem {} letras.'.format(nomeCompletoLen))
print('Seu primeiro nome tem {} letras.'.format(nomePrimeiro))
