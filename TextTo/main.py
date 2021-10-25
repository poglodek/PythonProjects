import gtts
import os
import requests
from playsound import playsound
from bs4 import BeautifulSoup
from random import randrange
from google_images_download import google_images_download  

text_file_name = "text.txt"
audio_file_name = "Audio.mp3"
text_file =""
distinct_words = [] 
distinct_words_index = 0

if os.path.isdir("./audio") == False:
    os.mkdir("./audio")

with open(text_file_name) as text:
    text_file = text.read()
words = text_file.replace("\n"," ").split(" ")
distinct_words = list(set(words))

print("Record a audio")
for word in distinct_words:
    distinct_words_index += 1
    print(distinct_words_index/len(distinct_words)*100)
    if word == "":
        continue
    tts = gtts.gTTS(str(word), lang="pl")
    tts.save("./audio/"+ word + ".mp3")

print("Recored audio")



if os.path.isdir("./photos") == False:
    os.mkdir("./photos")

distinct_words_index = 0
print("Starting downloading all images required to make a video")
for word in distinct_words:
    URL = "https://www.google.co.in/search?q="+word+"&source=lnms&tbm=isch"
    page = requests.get(URL)
    content = page.content
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("img")
    if len(results) == 1 or results[1] == "":
        continue
    photo = results[1]['src']

    response = requests.get(photo)
    file = open("./photos/" + word + ".jpg", "wb")
    file.write(response.content)
    file.close()

    distinct_words_index += 1
    print(distinct_words_index/len(distinct_words)*100)
print("Images downloaded")
