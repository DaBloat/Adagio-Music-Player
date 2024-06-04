import urllib.request as ytsearch
import re
from pytube import YouTube
from vlc import Instance
from time import sleep

instance = Instance()
player = instance.media_player_new()
queue_songs = []

songs = int(input('How many Songs you want to queue?: '))
for i in range(songs):
    search = input("Search for a song: ")
    html = ytsearch.urlopen(f'https://www.youtube.com/results?search_query={search.replace(" ", "+")}')
    vidID = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    print(vidID)
    link = f"https://www.youtube.com/watch?v={vidID[0]}"

    yt = YouTube(link)
    yt.streams.filter(only_audio=True)
    pop = [i for i in yt.streams.filter(only_audio=True)]

    stream = pop[-1]
    queue_songs.append(stream)

print(queue_songs[0].url)
for songs in queue_songs:
    media = instance.media_new(songs.url)
    player.set_media(media)
    player.play()
    sleep(1.5)
    print(f"Playing {songs.title} by Adagio Music Player")
    duration = player.get_length() / 1000
    sleep(duration)