import pygame
import os
import threading
import time
from flask import Flask
app = Flask(__name__)
ENDEVENT=42

paused = 0

playlist = os.listdir('./playlist')
print (playlist)

songNo = 0
lastSongNo = 0;

pygame.init()
pygame.mixer.init()

print("python pygame initialized!")


def paused():
	while paused==1:
		pass
	

def init():
	pygame.mixer.music.set_endevent(ENDEVENT)
	print("Initialising player...")
	play(playlist[0])

def play(filename):
	global songNo
	global paused
	songNo += 1
	pygame.mixer.music.load('./playlist/'+filename)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		#while paused==1:
		#	time.sleep(0.100)
		pygame.time.Clock().tick(1000)
		#time.sleep(0.5)
	
	if songNo > len(playlist)-1:
		songNo=0
	play(playlist[songNo])

def start_server():
	if __name__ == "__main__":
		app.run('0.0.0.0', 3000)

def loop():
	while True:
		time.sleep(1)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/pause")
def pause():
	global paused
	paused = 1
	pygame.mixer.music.pause()
	return "Paused"

@app.route("/add",methods=['POST'])
def add():
	return "Added track!"
	

@app.route("/resume")
def resume():
	global paused
	paused = 0
	pygame.mixer.music.unpause()
	return "Resumed"

serverTh = threading.Thread(target=start_server)
playerTh = threading.Thread(target=init)
playerTh.daemon = True
serverTh.daemon = True
serverTh.start()
playerTh.start()


loop()

#if __name__ == "__main__":
#	app.run('0.0.0.0',3000)








 
