import pygame
import os

playlist = os.listdir('./playlist')
print (playlist)

pygame.init()
pygame.mixer.init()

print("python pygame initialized!")



def init():
	print("Initialising player...")
	play(playlist[0])	

def play(filename):
	pygame.mixer.music.load('./playlist/'+filename)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(1000)

init()


 
