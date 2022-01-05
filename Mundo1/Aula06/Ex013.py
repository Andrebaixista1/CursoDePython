prod = float(input('Qual o seu salario ? R$'))
desc = prod + (prod*15/100)
print('O salário de R${:.2f} com 15% de aumento o valor muda para {:.2f}'.format(prod,desc))