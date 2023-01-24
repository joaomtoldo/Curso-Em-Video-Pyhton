'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

prod = ('Caneta', 1.4,
        'lápis', 1,
        'Compasso', 5,
        'Lapiseira', 4.75,
        'Borracha 2 cores', 0.95,
        'Apontador', 2.45,
        'Régua 30 cm', 6.5)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f'{prod[item]:_<30}', end='')
    else:
        print(f'R${prod[item]:>7.2f}')
print('-'*40)
