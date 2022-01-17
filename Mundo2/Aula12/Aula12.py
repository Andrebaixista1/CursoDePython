nome = str(input('Digite seu nome: '))

if nome == 'André':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Seu nome feminino')
else:
    print('Tenha um bom dia, {}!'.format(nome))
