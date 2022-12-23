# Elaborar um programa que determine o valor do produto
# considerando seu preço normal e condição de pagamento
# à vista/dineiro ou cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# em 3x ou mais no cartáo 20% de juros.

print("{:=^60}".format(' Lojas Toldo '))
preconorm = float(input("Qual o preço normal do produto? "))
condicao = input(''' Escolha uma opção de pagamento: 
 Opção | Condiçao de pagamento
   1   | à vista.
   2   | à vista no cartão.
   3   | em até 2 vezes no cartão.
   4   | em 3 vezes ou mais no cartão.
    qual opção deseja? ''')
if int(condicao) == 1:
    precofinal = (preconorm - (preconorm * 10 / 100))
elif int(condicao) == 2:
    precofinal = (preconorm - (preconorm * 5 / 100))
elif int(condicao) == 3:
    parcela = preconorm /2
    precofinal = preconorm
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif int(condicao) == 4:
    precofinal = preconorm + (preconorm * 20 / 100)
    prestacao = input('Em quantas vezes você quer pagar? ')
    parcela = int(precofinal) / int(prestacao)
    print('Sua Compra será parcelada em {}x de R${}'.format(prestacao,parcela))
else:
    precofinal = preconorm
    print("Opção inválida, Re-inicie o programa")
print("O valor final do produto será de R${:.2f}".format(precofinal))