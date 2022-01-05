velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')

