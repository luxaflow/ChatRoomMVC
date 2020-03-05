from libaries.Controller import Controller
import threading

class ServerController(Controller):

    """
    Controller regelt opstarten van Server
    Server moet luisteren in thread om gebruik van view voort te zetten
    """
    def __init__(self, window):
        Controller.__init__(self, window)

        self.__model = self.load_model('Server')
        self.__server = self.__model(self._env['HOST'], int(self._env['PORT']))

        self.__view = self.load_view('ServerView')

        self._window.load_frame(self.__view, self)
        self._current_view.set_labels(self._env['HOST'], self._env['PORT'])

        self.set_log_name(self._env['SERVER_LOG'])
        self.write_log('Server Starting Listening Thread: Host->{0} Port->{1}'.format(self._env['HOST'], self._env['PORT']))

        threading.Thread(target=self.start_listening).start()
        

    def start_listening(self):
        self.__server.listen()


           



    
