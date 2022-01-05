# Preço da passagem 

kmDePassagem = float(input("Digite a distância da viagem: "))
if kmDePassagem <= 200:
    preco = kmDePassagem * 0.50
    print("O preço da passagem é R$ {:.2f}".format(preco))
else:
    preco = kmDePassagem * 0.45
    print("O preço da passagem é R$ {:.2f}".format(preco))