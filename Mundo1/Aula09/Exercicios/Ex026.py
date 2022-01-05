
frase = input('Digite uma frase: ').upper()
letraA = frase.count('A')
posicaoA = frase.find('A')
posicaoUltimaA = frase.rfind('A')

print('A letra "a" aparece {} vezes na frase.'.format(letraA))
print('A primeira letra "a" aparece na posição {}.'.format(posicaoA))
print('A última letra "a" aparece na posição {}.'.format(posicaoUltimaA))