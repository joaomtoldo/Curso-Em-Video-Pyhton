''' refaça o ex 09 mostrando a tabuada de um numero usando um laço for '''

n = int(input('Digite um numero para calcular sua tabuada até 10: '))
print("A tabuada do {} até 10 é :".format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
