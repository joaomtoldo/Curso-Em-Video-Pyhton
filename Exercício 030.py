# Crie um programa que lia um numero inteiro e mostre se ele é par ou impar.

num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print("O numero {0} é par".format(num))
else:
    print('O numero {} é impar'.format(num))
print('--- F I M ---')
