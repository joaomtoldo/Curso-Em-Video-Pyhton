'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
 programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

print('-' * 25)
print('Cadastre uma Pessoa'.center(25))
print('-' * 25)
tot18 = toth = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo M/F: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN': 
        resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {tot18}.')
print(f'O total de homens cadastrados foi {toth}.')
print(f'O total de Mulhers com menos de 20 anos é {totm20}.')
print('Acabou !!!')
