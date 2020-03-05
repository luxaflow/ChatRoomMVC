import sys, os

class Core(object):

    def __init__(self):
        """
        Omdat all bestanden in sub-mappn leven
        Moeten het pad van waaruit de applicatie draait geewijzigd worden
        Hiermee worden het basis pad terug gezet naar 1 map hoger
        """
        sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

        from controller.SelectController import SelectController

        """
        Opstarten van eerste Controller
        """
        self.__current_controller = SelectController()

