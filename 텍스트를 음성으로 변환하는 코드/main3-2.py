from gtts import gTTS
import pygame
import os
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text= "안녕하세요. 파이썬과 40개의 작품들 입니다. "

tts = gTTS(text=text, lang='ko')
tts.save("hi_2.mp3")
pygame.mixer.init()
pygame.mixer.music.load("hi_2.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)