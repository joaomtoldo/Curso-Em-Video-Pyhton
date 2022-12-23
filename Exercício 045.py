'''Crie um programa que faça o computador jogar jokenpô com vc'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' Suas Opções :
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha uma opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('-=-' * 9)
print('O Computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-' * 9)
if computador == 0:
    if jogador == 0:
        print('O jogo empatou !!!')
    elif jogador == 1:
        print('O jogador Venceu !!!')
    elif jogador == 2:
        print('o computador Venceu !!!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('O computador venceu !!!')
    elif jogador == 1:
        print('O jogo empatatou !!!')
    elif jogador == 2:
        print('O jogador venceu !!!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('O jogador venceu !!!')
    elif jogador == 1:
        print('O computador venceu !!!')
    elif jogador == 2:
        print('O jogo empatou !!!')
    else:
        print('Jogada inválida!')
