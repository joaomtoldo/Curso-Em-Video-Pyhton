'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
 você deve mostrar, para cada palavra, quais são as suas vogais.'''

words = ('crie', 'um', 'programa', 'que', 'tenha', 'uma',
         'tupla', 'com', 'varias', 'palavras', 'depois',
         'disso', 'voce', 'deve', 'mostrar', 'para', 'cada',
         'palavra', 'quais', 'sao', 'suas', 'vogais' )
for word in words:
    print(f'\na palavra "{word}" possui as vogais: ',end='')
    for i in range(0,len(word)):
        if word[i] in 'aeiou':
           print(word[i]+", ", end='')
