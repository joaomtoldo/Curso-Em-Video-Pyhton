'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

n = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão dessa P.A.: '))
termo = n
cont = 1
escolha = 10
total = 0
while escolha != 0:
    total += escolha
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    escolha = int(input('\n quantos termos a mais vc deseja ver? (digite 0 para encerrar): '))
print('fim da PA, forma mostados ',total,'termos exibidos')
