# adivinhar numero entre 0 e 5

import random
escolhaNumeros = int(input('Escolha um número entre 0 e 5: ')) 
pcNumber = random.randint(0, 5) # gera um número aleatório entre 0 e 5

print('O número escolhido foi {}'.format(pcNumber)) 
if escolhaNumeros == pcNumber:
    print('Parabéns você acertou!')
else:
    print('Você errou!')
