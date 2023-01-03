'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('-=-' * 10)
print('Vamos Jogar Par ou Impar!')
print('-=-' * 10)
while True:
    jogador = int(input('Escolha um Numero: '))
    comp = randint(0,10)
    total = jogador + comp
    choice = ' '
    while choice not in ('ipIP'):
        choice = str(input('Escolha Par(p) ou Impar (i): ')).strip().lower()[0]
    if total % 2 == 0:
        numero = str('Par')
    else:
        numero = str('Impar')
    print(f'Você Jogou {jogador} o computador jogou {comp}.')
    print(f'O Total é {total} portanto um numero {numero}.')
    if choice == 'p' and numero == 'Par':
        print('=' * 30)
        print('Parabens você Ganhou!!!!')
        print('=' * 30)
    elif choice == 'i' and numero == 'Impar':
        print('=' * 30)
        print('Parabens você Ganhou!!!!')
        print('=' * 30)
    else:
        print('=' * 30)
        print('Você Perdeu - FIM DE JOGO PARA VOCÊ')
        print('=' * 30)
        break