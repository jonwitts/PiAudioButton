#!/usr/bin/python3

import pygame
from time import sleep
from os import system
from signal import pause
from gpiozero import Button

shutdown_btn = Button(21, hold_time=4)
pygame.init()

def shutdownAudio():
    # stop all active mixer sounds from playing
    pygame.mixer.stop()
    
    # load our shutdown sound
    s = pygame.mixer.Sound("/PiAudioButton/audio_files/shutdown-sound.wav")
    # and play it
    s.play()
    # loop whilst mixer is busy
    while pygame.mixer.get_busy():
        sleep(0.05)
    
    # sound has stoped now shutdown
    system("sudo shutdown now -hP")

shutdown_btn.when_held = shutdownAudio
pause()
