''' faça um programa que leia um nnumero inteiro e diga se ele é primo ou não'''

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print("{}".format(c), end=' ')
print('\n\033[mo número {} é divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O numero {} não é primo.'.format(num))