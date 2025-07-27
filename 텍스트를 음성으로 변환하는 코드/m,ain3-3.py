from gtts import gTTS
import pygame
import os
import time


os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'myText.txt'

with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text= read_file, lang='ko')

tts.save("myText.mp3")

pygame.mixer.init()
pygame.mixer.music.load("myText.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.3)
