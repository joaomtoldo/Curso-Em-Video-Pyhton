# Crie um programa que leia três segmentos de reta e diga ao usuário se elas podem formar um triângulo
from time import sleep
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
print('Processando...')
sleep(3)
if a < b+c and a > b-c:
    print("Com retas dos tamanhos digitados é possível formar um triângulo.")
else:
    print('Que pena, com retas desses tamanhos não consigo formar um triângulo.')