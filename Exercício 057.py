'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Valor inválido, digite novamente M ou F: ')).upper().strip()[0]
if sexo == 'F':
    print('Sexo Feminino registrado com sucesso!')
else:
    print('Sexo Masculino registrado com sucesso!')
