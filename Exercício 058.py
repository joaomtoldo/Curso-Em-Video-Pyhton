'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0,10)
print('Sou seu computador e acabei de pensar em um numero entre 0 e 10')
escolha = str(input('Quer tentar adivinhar ? [s] sim / [n] não: ').upper())
acertou = False
cont = 0
if escolha == 'N':
    print('Que pena! Fim do programa')
elif escolha == 'S':
    while not acertou:
        palpite = int(input('Qual seu palpite?: '))
        cont += 1
        if palpite == computador:
            acertou = True
        else:
            if palpite < computador:
                print('Mais... Tente novamente.')
            else:
                print('Menos... Tente novamente')
    print('''Parabens voce digitou {} e eu havia pensado em {}, você precisou de {} tentativas'''.format(palpite, computador, cont))
