# Exercício Python 44: Elabore um programa que calcule o valor a 
# ser pago por um produto, considerando o seu preço normal e 
# condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
formaPagamento = int(input('Qual é a forma de pagamento? '))

if formaPagamento == 1:
    valorPago = valorProduto - (valorProduto * 10 / 100)
    print(f'O valor a ser pago é R${valorPago:.2f}')
elif formaPagamento == 2:
    valorPago = valorProduto - (valorProduto * 5 / 100)
    print(f'O valor a ser pago é R${valorPago:.2f}')
elif formaPagamento == 3:
    valorPago = valorProduto
    parcela = valorPago / 2
    print(f'O valor a ser pago é R${valorPago:.2f}')
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif formaPagamento == 4:
    valorPago = valorProduto + (valorProduto * 20 / 100)
    qtdParcelas = int(input('Quantas parcelas? '))
    parcela = valorPago / qtdParcelas
    print(f'O valor a ser pago é R${valorPago:.2f}')
    print(f'Sua compra será parcelada em {qtdParcelas}x de R${parcela:.2f} COM JUROS')