#Escreva um programa de faça o computador "pensar"em um numero inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('Olá este é o jogo de adivinhação.')
esc = str(input('Você quer jogar comigo? \nSe sim digite S, se não quiser digite N: ')).upper()
if esc == 'S':
    escolha = random.randint(0, 5)
    print('Legal vamos começar. Eu pensei em um numero inteiro de 0 a 5 \nAgora vc tenta advinhar mas você tem apenas uma chance.')
    print(escolha)
    palpite = int(input('Digite seu palpite: '))
    if palpite == escolha:
        print('Parabens você acertou eu pensei no numero {}'.format(escolha))
    else:
        print('Que pena você errou, eu pensei no mumero {}'.format(escolha))
else:
    print ('Que pena. fim do programa. ')
