''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random
nums = tuple(random.sample(range(100),5))
print(nums)
print(f'O maior valor sorteado foi {max(nums)}')
print(f'O menor valor sorteado foi {min(nums)}')