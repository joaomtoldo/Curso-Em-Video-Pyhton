'''Escreva um programa para aprovar o emprestimo bancário de uma casa. o programa
vai perguntar o valor da casa. o salário do comprador e em quantos anos ele vai pagar.
calcule o valor da prestação mensal sabendo que ela não pode excerder 30% do
salário ou então o empréstimo será negado'''
import time
from time import sleep
print("\033[35m-=-=-=-=-=-=- PROGRAMA PARA CÁLCULO DE FINANCIAMEMTO -=-=-=-=-=-=-\033[m")
casa = float(input('Digite o valor da casa que deseja financiar: '))
salario = float(input('Digite seu salário mensal: '))
anos = int(input('Em quantos anos deseja pagar este financiamnto? '))
while anos > 30:
    print('O prazo máximo para financimento são de 30 anos.')
    anos = int(input('Digite um novo prazo até o máximo de 30 anos.'))
prazo = anos*12
prestacao = casa/prazo
print('\033[36m . . . C A L C U L A N D O . . .\033[m')
time.sleep(5)
print('O valor da prestação para essas condições será de R${:.2f}'.format(prestacao))
print('\033[36m Verificando condições de Financiamento....\033[m')
time.sleep(3)
if prestacao <= (salario * 30/100):
    print('O seu financiamento foi \033[32m APROVADO\033[m')
    print('Você pagará {} prestações no valor de R${}'.format(prazo,prestacao))
elif prestacao > (salario * 30/100):
    print('Que pena seu fianciamento foi \033[31m NEGADO\033[m')
    print('Tente aumentar sua renda ou uma casa mais barata ;)')