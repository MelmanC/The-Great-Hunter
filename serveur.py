import socket
import threading

class Serveur:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 12800
        self.connexion = True
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serveur.bind((self.host, self.port))
        self.serveur.listen(1)
        #print("Le serveur ecoute à present sur le port {}".format(self.port))
        self.connexion_avec_client, infos_connexion = self.serveur.accept()
        #print("Connexion etablie avec le client {}".format(infos_connexion))
        self.connexion = True
        self.thread = threading.Thread(target=self.recevoir)
        self.thread.start()
        self.envoyer("Serveur lance : {}".format(infos_connexion))
    
    def recevoir(self):
        while self.connexion:
            msg_recu = self.connexion_avec_client.recv(1024)
            msg_recu = msg_recu.decode()
            if msg_recu.upper() == "FIN":
                self.connexion = False
                print("Fermeture de la connexion")
                self.connexion_avec_client.close()
                self.serveur.close()
            self.player2 = msg_recu
        
    def envoyer(self, msg):
        msg_a_envoyer = msg.encode()
        self.connexion_avec_client.send(msg_a_envoyer)