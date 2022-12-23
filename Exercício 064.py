'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = int(input('Digite um numero inteiro: '))
c = soma = 0
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite outro valor, (999 para finalizar o programa): '))
print('_-'*26)
print('Você digitou {} numeros e a soma entre eles é {}'.format(c,soma))