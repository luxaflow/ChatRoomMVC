from libaries.Controller import Controller
from libaries.View import View

class SelectController(Controller):
    
    """
    Controller regelt keuze tussen Client en Server
    """
    def __init__(self):
        Controller.__init__(self)

        self.write_log('ChatRoom app started')

        self.__view = self.load_view('SelectView')
        self._window = View()        
        self._window.load_frame(self.__view, self)
        self._window.mainloop()
        
        
    def start_client(self, event):
        
        self.write_log('Starting Client...')

        new_controller = self.load_controller('ConnectController')
        new_controller(self._window)


    def start_server(self, event):

        self.write_log('Starting Server...')

        new_controller = self.load_controller('ServerController')
        new_controller(self._window)

    
