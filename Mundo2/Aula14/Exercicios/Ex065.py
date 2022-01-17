resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
media = soma / quant
maior = max(n)
menor = min(n)

print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))