# # Listas

# # Tuplas ()
# # Listas []
import os

os.system('cls')
# num = [5,4,3,2] # Lista
# num[3] = 1 # Altera o valor da posição 3
# num.append(7) # Adiciona um valor na lista
# # num.sort() # Ordena a lista em ordem crescente
# num.sort(reverse=True) # Ordena a lista em ordem decrescente
# num.insert(2,2) # Insere um valor na posição 2
# # num.pop(2) # Remove o valor da posição 2
# if 10 in num:
#     num.remove(20) # Remove o valor 
# else:
#     print('Não existe o valor 10')


# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# # valores.append(5)
# # valores.append(4)
# # valores.append(3)

# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))


# print(f'{"*-=-*"}'*20)
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}... ')
# print('\nCheguei ao final da lista')

a = [2,3,4,7]
# b = a # Cria uma ligação entre as duas listas
b = a[:] # Cria uma cópia da lista
b[2] = 8 # Altera o valor da posição 2 da lista B e a lista A também

print(f'Lista A: {a}')
print(f'Lista B: {b}')