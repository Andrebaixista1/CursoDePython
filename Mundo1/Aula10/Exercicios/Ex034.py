# Aumento de salário

funcionarioRecebe = float(input('Digite o salário do funcionário: '))
if funcionarioRecebe <= 1250:
    novo = funcionarioRecebe + (funcionarioRecebe * 0.15)
else:
    novo = funcionarioRecebe + (funcionarioRecebe * 0.10)
print('O salário do funcionário é R${:.2f} e com o aumento R${:.2f}'.format(funcionarioRecebe, novo))