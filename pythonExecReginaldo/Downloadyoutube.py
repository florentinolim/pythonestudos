from pytube import YouTube

youtube = YouTube('https://www.youtube.com/watch?v=RjgoceBB6Ms&t=308s')

youtube.streams.get_highest_resolution().download()
print(youtube)