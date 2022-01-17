import datetime

anoDeNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = datetime.date.today().year
ano = anoAtual - anoDeNascimento

if ano < 18:
    print("Você ainda não tem 18 anos, não precisa se alistar.")
elif ano == 18:
    print('Você tem 18 anos, precisa se alistar imediatamente.')
elif ano > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(ano - 18))
