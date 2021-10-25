import os
import cv2
import gtts
import shutil
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


with open(text_file_name) as text:
    text_file = text.read()
words = text_file.replace("\n"," ").split(" ")
distinct_words = list(set(words))

print("Record a audio")
tts = gtts.gTTS(str(words), lang="pl")
tts.save(audio_file_name)

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


print("Creating a video")
distinct_words_index = 0
images = [img for img in os.listdir("./photos/") if img.endswith(".jpg")]
frame = cv2.imread(os.path.join("./photos/", images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 1, (width,height))
for word in words:
    if word == "." or word == "":
        continue
    video.write(cv2.imread("./photos/"+ word + ".jpg"))
    distinct_words_index += 1
    print(distinct_words_index/len(words)*100)
print("video ready")
video.release()
cv2.destroyAllWindows()
os.remove(audio_file_name)
shutil.rmtree('./photos')
