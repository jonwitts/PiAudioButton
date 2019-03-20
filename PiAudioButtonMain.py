#!/usr/bin/python3

import pygame
from time import sleep
from random import choice
#from os import system
#from signal import pause
from gpiozero import Button

audio_btn = Button(17)
pygame.init()

bg = pygame.mixer.Sound("./audio_files/background.wav")
bg.play(loops=-1) # loops indefinitely

random_audio = ['./audio_files/random1.wav', './audio_files/random2.wav', './audio_files/random3.wav', './audio_files/random4.wav']

while True:
    ranAud = pygame.mixer.Sound(choice(random_audio))
    ranAud.play()
    time.sleep(2.0)

#def shutdownAudio():
    # stop all active mixer sounds from playing
 #   pygame.mixer.stop()
    
    # load our shutdown sound
    
    # and play it
  #  s.play()
    # loop whilst mixer is busy
   # while pygame.mixer.get_busy():
    #    sleep(0.05)
    
    # sound has stoped now shutdown
    #system("sudo shutdown now -hP")

#shutdown_btn.when_held = shutdownAudio
#pause()
