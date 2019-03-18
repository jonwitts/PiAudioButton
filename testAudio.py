#!/usr/bin/python3

import pygame
from signal import pause

pygame.init()

s = pygame.mixer.Sound("./audio_files/shutdown-sound.wav")
s.play()

pause()
