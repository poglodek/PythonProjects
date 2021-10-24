import gtts
from playsound import playsound

text_file_name = "text.txt"
audio_file_name = "Audio.mp3"

with open(text_file_name) as text:
    tts = gtts.gTTS(text.read(), lang="pl")
    tts.save(audio_file_name)

playsound(audio_file_name)
