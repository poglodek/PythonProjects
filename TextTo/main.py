import gtts
import os
import requests
from playsound import playsound
from bs4 import BeautifulSoup

text_file_name = "text.txt"
audio_file_name = "Audio.mp3"
text_file =""



with open(text_file_name) as text:
    text_file = text.read()

tts = gtts.gTTS(text_file, lang="pl")
tts.save(audio_file_name)

words = text_file.replace("\n"," ").split(" ")

print(words)


os.remove(audio_file_name)