# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h. mostre uma mensagem  dizendo que le foi multado
# A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Digite a velocidade do veículo em Km/h: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade de 80Km/h')
    print('O valor da multa é R${0:.2f}'.format((vel-80)*7))
else:
    print("Parabéns você é um motorista responsável, não ultrapassou o Limite de velocidade da pista")
