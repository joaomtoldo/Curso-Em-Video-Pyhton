'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

maior = menor = cont = soma =  0
choose = 's'
while choose == 's':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    choose = input('Deseja continuar a digitar Valores [ S / N ]: ').lower().strip()[0]
print ('Voce digitou {} e a média foi de {:.1f}, maior valor foi  {} e o menor foi {}'.format(cont,(soma/cont),maior,menor))
