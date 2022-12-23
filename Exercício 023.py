# crie um programa que leia um numero 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: digite um numero: 1834
#resultado::
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1


numero = str(input('Digite um número de 0 a 9999: '))
if len(numero) == 1:
    print('Unidade: '+ numero[(len(numero)-1)])
elif len(numero) == 2:
    print('Unidade: '+ numero[(len(numero) - 1)])
    print('Dezena: '+ numero[(len(numero)-2)])
elif len(numero) ==3:
    print('Unidade: ' + numero[(len(numero) - 1)])
    print('Dezena: ' + numero[(len(numero) - 2)])
    print('Centena: ' +numero[(len(numero) - 3)])
else:
    print('Unidade: ' + numero[(len(numero) - 1)])
    print('Dezena: ' + numero[(len(numero) - 2)])
    print('Centena: ' + numero[(len(numero) - 3)])
    print('Centena: '+ numero[(len(numero)-4)])