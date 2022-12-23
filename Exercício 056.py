'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
homemvelho = ""
homemidade = 0
mulhermenos20 = 0
for c in range(1,5):
    print('----- {} Pessoa -----'.format(c))
    nome = str(input('Nome: '.format(c))).strip()
    idade = int(input('Idade: '.format(nome)))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if sexo in "Mm":
        if idade > homemidade:
            homemidade = idade
            homemvelho = nome
    if sexo in "Ff" and idade < 20:
        mulhermenos20 += 1
print('O homem mais é {} e ele tem {} anos.'.format(homemvelho,homemidade))
print('A média de idade das 4 pessoas é {:.1f} anos'.format(somaidade/4))
print('{} mulheres tem menos de 20 anos.'.format(mulhermenos20))
