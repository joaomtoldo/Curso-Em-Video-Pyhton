'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
n1 = int(input('Digite um numero para calcular seu fatorial: '))
resultado = 1
cont = n1
print('{} ! = '.format(n1), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print('{}'.format(resultado))







#utilizando módulo:
#from math import factorial
#n = int(input('Digite um numeros para calcular seu fatorial'))
#f = factorial(n)
#print('{}! é igual a {}'.format(n,f))