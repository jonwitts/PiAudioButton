#!/usr/bin/python3

import pygame
from time import sleep
from random import choice
from gpiozero import Button

audio_btn = Button(17)
pygame.init()

bg = pygame.mixer.Sound("./audio_files/background.wav")
bg.play(loops=-1) # loops indefinitely

random_audio = ['./audio_files/random1.wav', './audio_files/random2.wav', './audio_files/random3.wav', './audio_files/random4.wav']

while True:
    if audio_btn.is_pressed:
        ranAud = pygame.mixer.Sound(choice(random_audio))
        ranAud.play()
        sleep(2)
