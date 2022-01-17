# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Digite um valor 1: '))
valor2 = int(input('Digite um valor 2: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('A soma de {} + {} é {}'.format(valor1, valor2, valor1 + valor2))
    elif opcao == 2:
        print('A multiplicação de {} x {} é {}'.format(valor1, valor2, valor1 * valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print('{} é maior que {}'.format(valor1, valor2))
        else:
            print('{} é maior que {}'.format(valor2, valor1))
    elif opcao == 4:
        valor1 = int(input('Digite um valor 1: '))
        valor2 = int(input('Digite um valor 2: '))


print('Finalizando...')

   