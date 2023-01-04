'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
barato = ' '
totc = totp1000 = menor = cont = 0
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    totc += preco
    cont += 1
    if preco > 1000:
        totp1000 += 1
    if cont == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {totc:.2f}.')
print(f'Temos {totp1000} produtos que custam mais de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
