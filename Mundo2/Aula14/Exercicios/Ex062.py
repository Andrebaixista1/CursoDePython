# Exercício Python 62: Melhore o DESAFIO 61, perguntando para 
# o usuário se ele quer mostrar mais alguns termos. O programa 
# encerrará quando ele disser que quer mostrar 0 termos.

print('='*30)
print('PROGRESSÃO ARITMÉTICA')
print('='*30)

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' → ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM')



