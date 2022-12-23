''' faça um programa que calcule a soma entre todos o números impares que são multiplos de tres e que se encontram no intervalo de 1 a 500'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} numeros solicitados é {}'.format(cont, soma))
