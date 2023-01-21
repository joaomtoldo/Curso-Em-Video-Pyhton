''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
while True:
    n = int(input('Digite um numero para mostrar sua tabuada até 10: '))
    print('-'* 50)
    if n < 0:
        break
    for i in range (1, 11):
        print(f'{n} x {i} = {(n*i)}')
    print('-'* 50)
print('Programa de tabuada encerrado.')