import importlib
from libaries.View import View
from helpers.Config import Config
from helpers.Log import Log

class Controller(Config, Log):
    """
    Hoofd controller klasse
    Deze klasse dient door elke controller overrft te worden
    hiermee wordt standaar functionaleit beeschikbaar gesteld
    """
    def __init__(self, window=None):
        Config.__init__(self)
        Log.__init__(self)
 
        self._controller_path = 'controller'
        self._model_path = 'model'
        self._view_path = 'view'

        self._window = window
        self._current_view = None


    """
    Het instellen van de huidige View
    hiermee is het mogelijk acties vanuit de controller op de View uit te voeren
    """
    def set_current_view(self, current_view):
        self._current_view = current_view

    """
    Het mogelijk maken voor het vinden en laden van modules
    Alle controllers hebben deze acties nodig
    """
    def load_controller(self, name):   

        module      = self.get_module(self._controller_path, name)
        instance = getattr(module, name)

        return instance


    def load_model(self, name):

        module      = self.get_module(self._model_path, name)
        instance       = getattr(module, name)

        return instance
        

    def load_view(self, name):

        module      = self.get_module(self._view_path, name)
        instance    = getattr(module, name)

        return instance

    """
    Het zoeken van modules in de daarvoor gemaakte mappen
    """
    def get_module(self, module_type, module_name):

        path = '{0}.{1}'.format(module_type, module_name)
        module = importlib.import_module(path)

        return module



