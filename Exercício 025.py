# Crie Um progama que leia o nme de uma pessoa e diga se ela em ~Silva`no nome.

nome = str(input('Digite o seu nome completo: ')).title()

if 'Silva' in nome:
    print('Parabêns você é da Familia Silva')
else:
    print('Que pena você não faz parte da familia Silva')
