'''Refaça o desafio 035 dos trinângulos
acrescentando o recurso de mostrar que tipo de trinagulo
será formado
Equilatero: todos os lados iguais.
Isósceles: dois lados iguais.
Escaleno: todos os diferentes.'''

from time import sleep
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
print('Processando...')
sleep(1)
if a < b+c and b < a + c and c < a + b:
    print('Com retas dos tamanhos digitados é possível forma um trinagulo' ,end='')
    if a == b == c:
        print(" Equilátero.")
    elif a != b != c != a:
        print(' Escaleno.')
    else:
        print (' Isóceles.')
else:
    print('Que pena, com retas desses tamanhos não consigo formar um triângulo.')
