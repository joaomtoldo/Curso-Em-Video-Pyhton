# escreva um programa que lei o nome compleo de uma pessoa e escreve separadamento o rimeiro e o ultimo nome dessa pessoa.
# Ex: Ana Maria de Souza.
# primeiro = Ana
# ULtimo = Souza

nome = str(input('Digite seu nome completo: ')).title()
nomeList = nome.split()
print(len(nomeList))
print('Seu nome Completo é ' + nome)
print('Seu primeiro nome é {}'.format(nomeList[0]))
print('Seu ultimo nome é {}'.format(nomeList[len(nomeList)-1]))