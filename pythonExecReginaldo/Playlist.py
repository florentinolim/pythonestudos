from pytube import Playlist, YouTube

playlist = Playlist("https://www.youtube.com/c/HashtagPrograma%C3%A7%C3%A3o/playlists")

for video in playlist:
    youtube = YouTube(video)

    youtube.streams.get_highest_resolution().download()