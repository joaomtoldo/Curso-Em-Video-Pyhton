# faça um programa que leia um ano e diga se ele é bissexto.

from datetime import date
ano = int(input("Digite o ano que você quer saber se é bissexto`, digite 0 para o ano atual: "))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano %400 == 0):
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print( 'o ano de {} não é Bissexto'.format(ano))
