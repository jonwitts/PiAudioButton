#!/usr/bin/python3

import pygame
from time import sleep
from random import choice
from os import system
from signal import pause
from gpiozero import Button

audio_btn = Button(17)
shutdown_btn = Button(21, hold_time=4)

pygame.init()

bg = pygame.mixer.Sound("/PiAudioButton/audio_files/background.wav")
bg.set_volume(0.5) # set volume to 50%
bg.play(loops=-1) # loops indefinitely

random_audio = ['/PiAudioButton/audio_files/random1.wav', '/PiAudioButton/audio_files/random2.wav', '/PiAudioButton/audio_files/random3.wav', '/PiAudioButton/audio_files/random4.wav']

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

def randomAudio():
    # pick a random sound file
    ranSnd = pygame.mixer.Sound(choice(random_audio))
    # now play it
    ranSnd.play()
    # pause so the button can not
    # be pressed continually
    sleep(15)

audio_btn.when_pressed = randomAudio
shutdown_btn.when_held = shutdownAudio

pause()
