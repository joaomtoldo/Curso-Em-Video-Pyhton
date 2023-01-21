''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numextenso = ('zero', 'um', 'dois', 'três', 'quatro',
              'cinco', 'seis', 'sete', 'oito', 'nove',
              'dez', 'onze', 'doze', 'treze', 'quatorze',
              'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Este numero não é aceito. ', end='')
    print(f'Você digitou {num}, que por extenso é {numextenso[num]}')
    choice = str(input('Deseja continuar? S/N:'))
    if choice in 'nN':
        break




