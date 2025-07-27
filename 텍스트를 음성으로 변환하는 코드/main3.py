from gtts import gTTS
import os

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts= gTTS(text= text , lang='ko')
base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)
save_path = os.path.join(base_dir, "hi.mp3")

tts.save(save_path)
