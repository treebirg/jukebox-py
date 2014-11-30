import pygame
import os
from flask import Flask
app = Flask(__name__)
ENDEVENT=42

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run('0.0.0.0',3000)





playlist = os.listdir('./playlist')
print (playlist)

songNo = 0

pygame.init()
pygame.mixer.init()

print("python pygame initialized!")



def init():
	pygame.mixer.music.set_endevent(ENDEVENT)
	print("Initialising player...")
	play(playlist[0])	

def play(filename):
	global songNo
	songNo += 1
	pygame.mixer.music.load('./playlist/'+filename)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(1000)
	if songNo > len(playlist)-1:
		songNo=0
	play(playlist[songNo])

init()


 
