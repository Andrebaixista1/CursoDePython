# Exercício Python 43: Desenvolva uma lógica que leia o peso e a 
# altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e 
# mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

seuPeso = float(input('Digite seu peso (Kg): '))
seuAltura = float(input('Digite sua altura (m): '))
seuIMC = seuPeso / (seuAltura ** 2)

if seuIMC < 18.5:
    print('Você está abaixo do peso!')
elif seuIMC >= 18.5 and seuIMC <= 25:
    print('Você está no peso ideal!')
elif seuIMC > 25 and seuIMC <= 30:
    print('Você está com sobrepeso!')
elif seuIMC > 30 and seuIMC <= 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')