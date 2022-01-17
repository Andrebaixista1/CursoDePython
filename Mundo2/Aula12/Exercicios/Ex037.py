# Conversor de bases
print('''
    Para qual formato você deseja converter?
    [1] Binário
    [2] Octal
    [3] Hexadecimal
''')

numeroInt = int(input("Digite um número inteiro: "))
opcao = int(input("Digite a opção desejada: "))


if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numeroInt, bin(numeroInt)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numeroInt, oct(numeroInt)[2:]))
else:
    print('{} convertido para hexadecimal é igual a {}'.format(numeroInt, hex(numeroInt)[2:]))

    
