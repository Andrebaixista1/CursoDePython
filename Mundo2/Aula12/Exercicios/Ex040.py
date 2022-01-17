# média do aluno

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média < 5:
    print('Sua nota foi {:.1f} e você foi reprovado!'.format(média))
elif média >= 5 and média <= 6.9:
    print('Sua nota foi {:.1f} e você foi de recuperação!'.format(média))
else:
    print('Sua nota foi {:.1f} e você foi aprovado!'.format(média))
