# Par ou Impar

num = int(input('Digite um número: '))
numResto = num % 2
if numResto == 0:
    print('O número {} é par'.format(num))
    
else:
    print('O número {} é ímpar'.format(num))
    