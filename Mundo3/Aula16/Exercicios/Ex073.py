# Exercício Python 73: Crie uma tupla preenchida com os 20 
# primeiros colocados da Tabela do Campeonato Brasileiro de 
# Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.


lista = ('Palmeiras', 'Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos',
            'Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')

print(f'Times do Brasileirão são: {lista}', end=' ')
print(f'\nOs 5 primeiro são {lista[:5]}', end=' ')
print(f'\nOs 4 últimos colocados são {lista[-4:]}')
print(f'Em ordem alfabética fica {sorted(lista)}')

print(f'E o time Chapecoense está na {lista.index("Chapecoense")+1}ª posição')