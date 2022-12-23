'''Desemvolva um programa que leia o primeiro termo e a razão de um Progressão aritimética
no final mostre os 10 primeiros termos dessa prograssão'''

ptermo = int(input("Digite o primeiro termo da sua Progressão Aritimética (PA): "))
razao = int(input('Digite a razão desta PA: '))
termo = ptermo
print('Os dez primeiros termos dessa PA são :')
print(ptermo, end=', ')
for c in range(9):
    termo += razao
    print(termo, end=', ')

#primeiro = int(input('digite o primeiro termo: ')
#razao = int(input('digite a razão: ')
#decimo = primeiro + (10-1) * razao
#for c in range (primeiro, decimo, razao):
#   print('{}'.fomrat(c), end=" ")
#print('Acabou!')