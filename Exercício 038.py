''' Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela a seguinte mensagem:
o primero numero é o maior
o segundo numero é o maior
Não existe valor maior os dois são iguais'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print ('O primeiro número é o maior.')
elif num2 > num1:
    print('O segundo número é o maior.')
else:
    print('Não existe valor maior, os dois são iguais.')