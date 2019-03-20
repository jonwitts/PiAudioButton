#!/usr/bin/python3

import pygame
from time import sleep
from os import system

pygame.init()

# stop all active mixer sounds from playing
pygame.mixer.stop()

# load our shutdown sound
s = pygame.mixer.Sound("./audio_files/shutdown-sound.wav")
# and play it
s.play()
# loop whilst mixer is busy
while pygame.mixer.get_busy():
    #print("Mixer is busy")
    sleep(0.05)

# sound has stoped now shutdown
#print("shutting down now")
system("shutdown now -hP")
