from playsound import playsound
import threading

class Music:
    def __init__(self):
        self.thread = threading.Thread(target=self.music)
        self.thread.start()
    def music(self):
        while True:
            playsound("assets/Music.wav")
