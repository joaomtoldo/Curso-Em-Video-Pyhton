''' faca um programa que leia uma fraswe e diga se ela é um palindromo'''
frase = str(input('Digite uma frase:  ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('a Palavra {} ao contrario é {}'.format(junto, inverso))
if junto == inverso:
    print('Por Tanto temos um Palindromo')
else:
    print('Por tanto NÃO temos um Palindromo')


