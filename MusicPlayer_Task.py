import pygame
import os

def my_music(go):
    pygame.mixer.init()
    pygame.mixer.music.load(go)
    pygame.mixer.music.play()

def main():
    my_folder = "musicfolder"
    
    print("Available songs:")
    for file in os.listdir(my_folder):
        if file.endswith(".mp3"):
            print(file)

    song_name = input("Enter the name of the song you want to play (including the extension): ")
    song_path = os.path.join(my_folder, song_name)

    if os.path.exists(song_path):
        my_music(song_path)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
