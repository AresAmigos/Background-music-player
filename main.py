from pygame import mixer #pip install pygame
song = input("Enter the path of the song: ")
mixer.init()
mixer.music.load(song) #load the song
mixer.music.play() #start play the song
while True: #loop for song, if this doesn't exist the song will stop to play
    player = True #random value
