''' faca uma logia que leia um numero e diga os numeros primos entre 1 e o numero digitado.'''

num = int(input('Digite um numero: '))
print('Entre 1 e {} existem esses numeros primos: '.format(num))
for c in range(1, num +1):
    tot = 0
    for v in range(1, c+1):
        if c % v == 0:
            tot += 1
    if tot == 2:
        print(c, end=' ')