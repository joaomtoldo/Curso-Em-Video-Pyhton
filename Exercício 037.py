'''' Escreva um programa que leia um numero interio qualquer e peça para o usuário escolher qual será a base de conversão
1 binário
2 octal
3 hexadecimal'''
print('\033[7;90;46m ________COVERSOR DE BASES_________\033[m')
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Sua escolha: '))
if opcao == 1:
    print('O número {0} convertido para BINÁRIO é {1}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('A opção {} não é válida, por favor reinicie o programa!'.format(opcao))

