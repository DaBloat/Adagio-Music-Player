import urllib.request as ytsearch
import re
from pytube import YouTube
from vlc import Instance
from time import sleep

search = input("Search for a song: ")
html = ytsearch.urlopen(f'https://www.youtube.com/results?search_query={search.replace(" ", "+")}')
vidID = re.findall(r'watch\?v=(\S{11})', html.read().decode())
print(vidID)
link = f"https://www.youtube.com/watch?v={vidID[0]}"

yt = YouTube(link)
yt.streams.filter(only_audio=True)
pop = [i for i in yt.streams.filter(only_audio=True)]
#print(pop)
# stream = yt.streams.get_audio_only()

stream = pop[-1]
#print(stream.url)

instance = Instance()
player = instance.media_player_new()
media = instance.media_new(stream.url)
player.set_media(media)
player.play()
sleep(1.5)
print(f"Playing {stream.title} @ {link}")
duration = player.get_length() / 1000
sleep(duration)



