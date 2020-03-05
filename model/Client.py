import socket, threading, sys, pickle
from helpers.Log import Log
from helpers.Config import Config

class Client(Config, Log):
    """
    Config en Log klassen zijn nodig voor het loggen 
    """
    def __init__(self, controller):
        Config.__init__(self)
        Log.__init__(self, self._env['CLIENT_LOG'])
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__controller = controller

    """
    Het verbinden aan de server
    Tevens wordt een thread opgestart voer het ontvangen van data
    """
    def connect(self, host, port):
        
        try:
            self.__sock.connect((host, port))
        except socket.error as msg:
            self.write_log(msg, 'error')

        self.write_log('Starting Client receive thread')
        threading.Thread(target=self.receive).start()

    """
    Mogelijkheid voor het versturen van berichten naar de server
    """
    def send(self, message):
        
        try:
            self.__sock.sendall(message)
        except:
            self.write_log('Could not send message!', 'error')

    """
    Methode die in thread wordt onderhouden
    Ontvangt data van de Server
    """
    def receive(self):
        
        while True:

            data = self.__sock.recv(1024)

            if not data:
                sys.exit(0)
            
            self.write_log('Receiving Message...')
            self.__controller.receive_message(data)
            
        
