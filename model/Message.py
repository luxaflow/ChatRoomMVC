import pickle


class Message(object):
    """
    Klasse voor het opslaan van data
    Deze klasse kan vervolgens verstuurd worden
    """
    def __init__(self, user, message):
        self.__message = message
        self.__user = user

    def get_user(self):
        return self.__user

    def get_message(self):
        return self.__message