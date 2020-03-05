from libaries.Controller import Controller
import pickle

class ClientController(Controller):

    def __init__(self, window, user, host, port):
        Controller.__init__(self, window)
        

        self.__client_model = self.load_model('Client')
        self.__client = self.__client_model(self)

        self.set_log_name(self._env['CLIENT_LOG'])
        self.write_log('Connecting to Server: Host->{0} Port->{1} User->{2}'.format(host, port, user.get_username()))

        self.__client.connect(host, port)
        
        self.__msg = self.load_model('Message')
        self.__user = user

        self.__view = self.load_view('ClientView')
        self._window.load_frame(self.__view, self)


    def send_message(self, event):
        msg = self._current_view.get_message_var()

        self.write_log('Sending message...')
        message = self.__msg(self.__user, msg)

        self.__client.send(pickle.dumps(message))

    def receive_message(self, data):
        
        msg = pickle.loads(data)

        if msg.get_user().get_username() == self.__user.get_username():
            username = 'Me'
        else:
            username = msg.get_user().get_username()

        message = '{0}: {1}'.format(username, msg.get_message())
        self.write_log('Received message: From->{0} Message->{1}'.format(username, msg.get_message()))
        self._current_view.insert_message_box(message)
