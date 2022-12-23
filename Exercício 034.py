# Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para salários inferiores calcule um aumento de 15%.

salario = float(input('Digite o salário atual: '))
if salario <= 1250.00:
    print ('O salário com aumento será de {}'.format(salario*1.15))
else:
    print ('O salário com aumento será de {}'.format(salario*1.1))
