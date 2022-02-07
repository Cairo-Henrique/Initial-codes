from random import choice
import pygame
notas = ['do.mp3','re.mp3','mi.mp3','fa.mp3','sol.mp3','la.mp3','si.mp3']
for i in range(8):
    pygame.mixer.init()
    pygame.mixer.music.load(choice(notas))
    pygame.mixer.music.play()
