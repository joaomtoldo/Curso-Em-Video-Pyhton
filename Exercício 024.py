# Escreva um Prorama que lei ao nome de uma cidade e diga se ela começa com o nome "Santo".

name = str(input("Digite o nome de sua cidade: "))
namelimpolista = name.capitalize().strip().split()
if (namelimpolista[0] == 'Santo'):
    print("Parabêns o nome da sua cidade começa com {}".format(namelimpolista[0]))
else:
    print("Que pena sua cidade não começa com Santo.")