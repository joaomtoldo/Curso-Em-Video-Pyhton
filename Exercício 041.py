'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com a idade
Até 9 anos :mirim
até 14 anos : infantil
até 19 anos : junior
até 25 anos : senior
acima : master
'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Informe o ano de seu nascimento: '))
idade = ano_atual - ano_nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você esta na categoria Mirim.')
elif idade <= 14:
    print('Você esta na categoria infantil.')
elif idade <= 19:
    print('Você esta na categoria junior')
elif idade <= 25:
    print('Você esta na categoria senior')
elif idade > 25:
    print('Você esta na categoria Master')
