# cont = 1

# while cont <= 10:
#     print(cont,end=' -> ')
#     cont += 1
# print('Fim')



# n = s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# #print('A soma é {}'.format(s))
# print(f'A soma é {s}')


nome = "José"
idade = 23
salario = 1234.56
print(f'O {nome} tem {idade} anos') # f-string Python 3.6+
print('O {} tem {} anos'.format(nome, idade)) # string formatada Python 3
print('O %s tem %d anos' % (nome, idade)) # string formatada Python 2
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')