'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
se o valor digitado for impar desconsidere-o.'''
print("Somente os numeros pares serão somados.")
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero inteiro. '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
    else:
        print('Numero impar não será somado')
print('A soma dos {} numeros pares digitados é {}'.format(cont, soma))