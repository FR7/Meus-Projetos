# Faça um programa em Python que abra e reproduza o audio de um arquivo mp3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load("stone.mp3")
pygame.mixer.music.play()
input('Agora você escuta?')