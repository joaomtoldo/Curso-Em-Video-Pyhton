# Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem. Cobrando R$0.5. por km
# para viagens ate 200 Km e R$0.45 para viagens mais longas.

dist = float(input("Digite a distancia de sua Viagem: "))
if dist <= 200:
    custo = dist*0.5
else:
    custo = dist*0.45
print("Para esta viagem a passagem custa R${:.2f}.".format(custo))