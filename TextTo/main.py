import gtts
import os
import requests
from playsound import playsound
from bs4 import BeautifulSoup

text_file_name = "text.txt"
audio_file_name = "Audio.mp3"
text_file =""
distinct_words = [] 


with open(text_file_name) as text:
    text_file = text.read()

tts = gtts.gTTS(text_file, lang="pl")
tts.save(audio_file_name)

words = text_file.replace("\n"," ").split(" ")
print(words)

for word in words:
    if word  not in distinct_words:
        distinct_words.append(word)
print(distinct_words)
#wyrazy zescrapowac z zdj z google grafika a potem zrobić film

os.remove(audio_file_name)