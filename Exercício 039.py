'''Faç um programa que elia o ano de nascimento de um jvem e informe, de acordo com sua idade.
 se ele ainda vai se alistar ao serviço militar.
 se é a hora de se alista.
 sejá passou do tempo do alistamento
 seu programa deve mostrar tambem o tempo que falta ou que passou do prazo'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano em que você nasceu: '))
idade = ano_atual - ano_nasc
if idade == 18:
    print('''Parabéns esta na hora de você se alistar no serviço militar obrigatório
Procure a junta militar mais próxima de você.''')
elif idade > 18:
    print('''Humm, pareçe que já passou do tempo de você se alistar né,
Você tem {} anos isso quer dizer que voce se alistou, ou pelo menos deveriar ter se alistado ha {} anos.'''.format(idade,(idade-18)))
elif idade < 18:
    print('''Você tem só {} aninhos, ainda não esta pronto para as Forças Armadas Brasileiras
Mas não fique triste em {} anos nos veremos novamente he he he!!!'''.format(idade, (18-idade)))
