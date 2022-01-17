# Exercício Python 36: Escreva um programa para aprovar o 
# empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

salarioEm30 = salario * 0.3

if (valorCasa / (anos * 12) > salarioEm30):
    print('Para pagar uma casa de R${:.2f} em {} anos, o valor mensal será de R${:.2f}.'.format(valorCasa, anos, valorCasa / (anos * 12)))
    print('\033[31mEmpréstimo negado!\033[m')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, o valor mensal será de R${:.2f}.'.format(valorCasa, anos, valorCasa / (anos * 12)))
    print('\033[32mEmpréstimo aprovado!\033[m')