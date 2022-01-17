# Exercício Python 55: Faça um programa que leia o peso de cinco 
# pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesoMaior = 0
pesoMenor = 0

for p in range(1, 6):
    pesoPessoa = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        pesoMaior = pesoPessoa
        pesoMenor = pesoPessoa
    else:
        if pesoPessoa > pesoMaior:
            pesoMaior = pesoPessoa
        if pesoPessoa < pesoMenor:
            pesoMenor = pesoPessoa

print('O maior peso foi de {}kg.'.format(pesoMaior))
print('O menor peso foi de {}kg.'.format(pesoMenor))
