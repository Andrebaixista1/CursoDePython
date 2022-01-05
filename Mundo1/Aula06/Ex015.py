dias = float(input('Quantos dias foi alugado ?'))
km = float(input('Quantos Km foi rodado ?'))
print('O total a pagar é de R${:.2f}'.format(dias*60 + km*0.15))