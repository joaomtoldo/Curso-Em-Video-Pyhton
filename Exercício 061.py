'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
 da progressão usando a estrutura while.'''

n = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão dessa P.A.: '))
termo = n
cont = 1
while cont <= 10:
    print('{} '.format(termo), end='')
    termo += r
    cont += 1
