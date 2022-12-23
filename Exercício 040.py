'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando no final, de acordo com a media atinginda:
 média abaixo de 5.0:
 REPORVADO
 média entre 5.0 e 6.9:
 RECUERAÇÃO
 Média maior que 7.0
 APROVADO '''

print('\033[034mPROGRAMA PARA CÁLCULO DA MÉDIA\033[m')
n1 = float(input("Digite a primeira nota entre 0,0 e 10,0: "))
n2 = float(input('Digite a segunda nota: '))
print('\033[037mC A L C U L A N D O . . . \033[m')
media = float((n1+n2)/2)
from time import sleep
sleep(3)
if media < 5.0:
    print("Sua média foi de {:.1f} que pena você foi \033[031m REPROVADO\033[m".format(media))
elif 5.0 < media <6.9:
    print('Sua média foi de {:.1f} você esta da \033[033mRECUPERAÇÃO\033[m'.format(media))
elif media > 7.0:
    print('Sua média foi de {:.1f} parabéns foi foi \033[034mAPROVADO\033[m'.format(media))