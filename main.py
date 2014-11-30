import pygame, os, threading, time
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = './playlist/'
ALLOWED_EXTENSIONS = set(['ogg', 'mp3', 'wav'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

previousFile = None

ENDEVENT=42

paused = 0
songNo = 0
lastSongNo = 0



playlist = os.listdir('./playlist')
print (playlist)



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
	global previousFile
	global playlist
	songNo += 1
	
	previousFile = filename

	pygame.mixer.music.load('./playlist/'+ filename)
	print "Now playing " + filename

	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		#while paused==1:
		#	time.sleep(0.100)
		pygame.time.Clock().tick(1000)
		#time.sleep(0.5)
	
	if songNo > len(playlist)-1:
		songNo=0
	play(playlist[songNo])	
	print "Removed " + previousFile + " from the playlist"
	playlist.remove(previousFile)

def start_server():
	if __name__ == "__main__":
		app.run('0.0.0.0', 3000)

def loop():
	while True:
		time.sleep(1)

@app.route("/")


@app.route("/pause")
def pause():
	global paused
	paused = 1
	pygame.mixer.music.pause()
	return "Paused"
@app.route('/next', methods=['GET'])
def nextSong():
	global lastSongNo
	global previousFile
	if songNo < len(playlist) - 1:
			play(playlist[songNo + 1])
			lastSongNo = songNo + 1;
			previousFile = playlist[songNo]
			return "Song Changed"
	songNo = 0
	play(playlist[songNo])
	return "Playlist Restarted"
		
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/add', methods=['GET', 'POST'])
def upload_file():
	global playlist
	if request.method == 'POST':
	        file = request.files['file']
	        if file and allowed_file(file.filename):
	            filename = secure_filename(file.filename)
	            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	            if str(filename) not in playlist:
	            	playlist.append(filename)
	            	print(playlist)
	            return 'Working'
	return 'CURRENT RQS'

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








 
