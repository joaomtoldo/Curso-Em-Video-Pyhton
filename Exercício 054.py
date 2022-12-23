'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite o Ano de nascimento da {}ª pessoa: '.format(c)))
    if anoatual - ano >= 21:
        maior += 1
    else:
        menor += 1
print("\nAo todo tivemos {} pessoas maiores de idade.".format(maior))
print('E tivemos {} pessoas menores de idade. '.format(menor))
