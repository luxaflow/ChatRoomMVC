from libaries.Controller import Controller

class ConnectController(Controller):
    
    """
    Controller voor het verwerken van verbinding en gebruiker info
    Deze gegevens kunnen daarna door gegeven worden
    """
    def __init__(self, window):
        Controller.__init__(self, window)

        self.__user_model = self.load_model('User')

        self.__view = self.load_view('ConnectView')
        self._window.load_frame(self.__view, self)

        self._current_view.set_host_var(self._env['HOST'])
        self._current_view.set_port_var(self._env['PORT'])

    
    def get_host(self):
        return self.__host


    def get_port(self):
        return self.__port


    def connect(self, event):
        
        username = self._current_view.get_username_var()
        user = self.__user_model(username)

        self.__host = self._current_view.get_host_var()
        self.__port = self._current_view.get_port_var()

        self.set_log_name('client.log')
        self.write_log('Starting Client...')

        new_controller = self.load_controller('ClientController')
        new_controller(self._window, user, self.__host, self.__port)