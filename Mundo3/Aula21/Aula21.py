# Funções Parte 2

#################### Interactive Help - Ajuda Interativa
#  help(print)

################## Docstrings - Documentação de Funções

# def contador(i,f,p):
#     """
#     -> Função que realiza a contagem
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     c = i
#     while c <= f:
#         print(f'{c}',end=' ')
#         c += p
#     print('FIM!')

# contador(2,10,2)

# help(contador)
    
################## Parametros Opcionais

# def somar(a=0,b=0,c=0): 
#     """
#     -> Função que realiza a soma de três valores
#     :param a: O primeiro valor
#     :param b: O segundo valor
#     :param c: O terceiro valor
#     :return: A soma dos três valores
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3,2,5)
# somar(8,4)

################## Escopo de Variáveis

# def teste(n):
#     x = 8
#     print(f'Na função teste o x vale {x}')
#     print(f'Na função teste o n vale {n}')

# n = 2
# print(f'No programa principal n vale {n}')
# teste()
# print(f'No programa principal x vale {x}')

# def teste2(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')



# a = 5
# teste2(a)
# print(f'A fora vale {a}')


################## Retorno de Valores

#### Exemplo 1 ####
# def somar(a=0,b=0,c=0): 
#     s = a + b + c
#     return s

# r1 = somar(3,2,5)
# r2 = somar(2,2)
# r3 = somar(6)
# print(f'Os valores retornados foram {r1}, {r2} e {r3}')

#### Exemplo 2 ####
# def fatorial(num =1):
#     f = 1
#     for c in range(num,0,-1):
#         f *= c
#     return f

# # n = int(input('Digite um número: '))
# # print(f'O fatorial de {n} é igual a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()

# print(f'Os resultados são {f1}, {f2} e {f3}')

#### Exemplo 3 ####

def ParOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
# print(f'O número {num} é {ParOuImpar(num)}')
if ParOuImpar(num):
    print('É par!')
else:
    print('É impar!')