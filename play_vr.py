import time
import pygame
def play_vr(file):
    process_id=4
    pygame.mixer.init()
    pygame.mixer.music.load(open(file,"rb"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
