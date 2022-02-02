# Exercício Python 72: Crie um programa que tenha uma tupla 
# totalmente preenchida com uma contagem por extenso, de 
# zero até vinte. Seu programa deverá ler um número pelo 
# teclado (entre 0 e 20) e mostrá-lo por extenso.
# while True:
#     num = int(input('Digite um número de 0 a 20: '))
#     cont = ('zero','um','dois','tres','quatro',
#             'cinco', 'seis', 'sete','oito','nove',
#             'dez','onze','doze','treze','catorze',
#             'quinze','dezesseis','dezessete','dezoito',
#             'dezenove','vinte')

#     tuplaNum = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#     if num in tuplaNum:
#         print(f'O número {num} por extenso é {cont[num]}')
#         break
#     else:
#         break

# Outra forma

cont = ('zero','um','dois','tres','quatro',
            'cinco', 'seis', 'sete','oito','nove',
            'dez','onze','doze','treze','catorze',
            'quinze','dezesseis','dezessete','dezoito',
            'dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamete ', end='')
print(f'Você digitou o número {cont[num]}')