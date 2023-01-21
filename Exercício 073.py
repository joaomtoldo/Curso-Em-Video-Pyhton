''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético -MG',
                 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
                 'Cuibá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-=-' * 15)
print('Os 5 Primeiros colocados são: ')
print(classificacao[0:5])
print('-=-' * 15)
print('Os últimos 4 colocados são:')
print(classificacao[16:20])
print('-=-' * 15)
print('os time em ordem alfabética: ')
for time in sorted(classificacao):
    print(time)
print('-=-' * 15)
print('A chapecoense não esta entre os 20 primeiros colocados')
print('-=-' * 15)