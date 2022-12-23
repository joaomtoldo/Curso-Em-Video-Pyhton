# Escreva um programa que leia três numeros e diga qual é o maior e qual é o menor

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('Digite o terceiro numero: '))
menor = x
# Verificando o menor numero.
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
# Verificando o maior numero.
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z

print('O menor numero digitado foi {}.'.format(menor))
print('O maior numero digitado foi {}.'.format(maior))
