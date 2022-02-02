from cgi import test
import os
os.system('cls')

####################### Exemplo 1 ############################
# teste = list()
# teste.append('André')
# teste.append(25)

# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])

# print(galera)

####################### Exemplo 2 ############################
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# # print(galera[0][0])
# for p in galera:
#     # print(p[0])
#     print(f'{p[0]} tem {p[1]} anos de idade.')

####################### Exemplo 3 ############################

totmai = totmen = 0

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

# print(galera)
print('-=' * 30)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maior e {totmen} menores de idade')