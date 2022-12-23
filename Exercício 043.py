''' Desenvolva uma lógica que leia o peso e a altura de uma pesoa e
calcule o seu IMC e mostre seu status de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25 : peso ideal
entre 25 e 30 : sobre peso
entre 30 e 40 : obesidade
acima de 40 obesidade mórbida'''
print ('''____________________________________________________
             
             C Á L C U L O   D O   I M C
____________________________________________________''')
altura = float(input("Digite sua altura (m): "))
peso = float(input("Digite o seu peso (Kg): "))
imc = (peso/(altura ** 2))
print('CALCULANDO....')
from time import sleep
sleep(1)
print('Seu IMC é de {:.1f}.'.format(imc), end='')
if imc < 18.5:
    print(' Você esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(' Você esta no peso ideal')
elif 25 <= imc < 30:
    print(' Você com sobre peso')
elif 30 <= imc < 40:
    print(' Você esta obeso')
else:
    print(' Você esta em Obesidade Mórbida')
