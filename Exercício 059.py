'''Crie um programa que leia dois valores e mostre um menu na tela:'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('o maoir numero é {}'.format(n1))
        elif n2 > n1:
            print('o maior numero é {}'.format(n2))
        else:
            print ('os dois numeros são iguais.')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('acabou')
    else:
        print('Opção inválida. tente novamente.')
    print('=-='*15)
print('Fim do programa!')