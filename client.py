import socket
import threading

class Client:
    def __init__(self,ip=""):
        self.host = ip
        self.port = 12800
        self.connexion = True
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        print("Client lance : {}".format(self.port))
        self.thread = threading.Thread(target=self.recevoir)
        self.thread.start()
    
    def recevoir(self):
        while self.connexion:
            msg_recu = self.client.recv(1024)
            msg_recu = msg_recu.decode()
            if msg_recu.upper() == "FIN":
                self.connexion = False
                print("Fermeture de la connexion")
                self.client.close()
            self.player2 = msg_recu #ICIIIIIIIIIIIIIIIIIII
    
    def envoyer(self, msg):
        msg_a_envoyer = msg.encode()
        self.client.send(msg_a_envoyer)