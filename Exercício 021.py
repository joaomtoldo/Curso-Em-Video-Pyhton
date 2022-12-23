#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


from pygame import mixer
mixer.init()
mixer.music.load("iron.mp3")
mixer.music.set_volume(1)
mixer.music.play()
input()

while True:
    print('Pressione (p) para pausar a musica, (c) para continuar, (s) para parar e sair do programa ')
    comando = input()

    if comando == "p":
        mixer.music.pause()

    if comando == "c":
        mixer.music.unpause()

    if comando == "s":
        mixer.music.stop()
        break
