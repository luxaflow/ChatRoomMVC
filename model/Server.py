import threading, socket, pickle
from helpers.Log import Log
from helpers.Config import Config

class Server(Config, Log):
    """
    Klasse die de binnenkomende verbinding kan accepteren
    Tevens kunnen hierin de verbindingen in threads worden opgeslagen
    """
    def __init__(self, host, port):
        Config.__init__(self)
        Log.__init__(self, self._env['SERVER_LOG'])

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connections = []
        self.__host = host
        self.__port = port

    """
    Start het luisteren naar verbindingen
    Onderhoud een loop met blocking accept welke wacht op verbindingen
    Start een nieuwe thread voor elke client die verbind
    """
    def listen(self):

        try:
            self.__sock.bind((self.__host, self.__port))
        except socket.error as msg:
            self.write_log('Bind failed. {0}'.format(msg), 'error')

        self.__sock.listen(10)
        self.write_log('Server listening: Host->{0} Port->{1}'.format(self.__host, self.__port))

        while True:

            conn, addr = self.__sock.accept()
            threading.Thread(target=self.recv_thread, args=(conn, addr)).start()

        self.__sock.close()


    """
    Methode die voor elke Client in eeen thread leeft
    Tevens worden hiermee de threads in variablen opgeslagen
    Berichten kunnen zo naar elke client geestuurd worden
    """
    def recv_thread(self, conn, addr):

        self.write_log('connection from: {0} on port {1}'.format(addr[0], str(addr[1])))

        if conn not in self.__connections:
            self.__connections.append(conn)

        while True:

            data = conn.recv(1024)
            if not data:
                break

            msg = pickle.loads(data)
            self.write_log('Receive message: From->{0} Message->{1}'.format(msg.get_user().get_username(), msg.get_message()))

            for c in self.__connections:
                c.sendall(data)
