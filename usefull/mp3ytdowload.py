#mp3 youtube downloader
#install pytube (type in cmd or terminal "pip install pytube")
from pytube import YouTube
from sys import argv
link = input("give yt link: ")
yt = YouTube(link)
print("Title: ", yt.title)
yd2 = yt.streams.get_audio_only()
#put the path of the location where the the audio will be dowloaded
yd2.download('C:/Users/sfar/Music/yt mp3')