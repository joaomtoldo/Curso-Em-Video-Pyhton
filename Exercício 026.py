# escreva um programa que leia uma frase pelo telado e mostre:
# 1 Quantas vezes aparece a letra 'A'.
# 2 em que posiçao ela aparece a primera vez.
# 3 em que posição ela aparece pela ultima vez.

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece pela primenra vez no indice {} e pela ultima vez no indice {}.'.format(frase.find('A'), frase.rfind('A')))