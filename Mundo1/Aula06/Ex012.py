prod = float(input('Qual o preço do produto ? R$'))
desc = prod - (prod*5/100)
print('O produto de R${} com 5 de desconto o valor cai para {:.2f}'.format(prod,desc))