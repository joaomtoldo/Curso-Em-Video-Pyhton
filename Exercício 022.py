# Crie um Programa que leia o nome completo de uma pessoa e mostre:
# 1 o nome com todas as letras maiúsculas
# 2 o NOme com todas as letras minúsculas
# 3 Quantas letras ao todo (sem considerar os espaços)
# 4 Quantas letras tem o primeiro nome.

name: str = input('Digite seu nome completo:')
print('Olá '+name)
print('seu nome com todas as letras maiúsculas: ',name.upper())
print('seu nome com todas as letras minúsculas: ',name.lower())
print('Seu nome tem {} letras'.format(len(name)-name.count(' ')))
lista = name.split()
print('Seu primeiro nome tem {} letras'.format(len(lista[0])))
