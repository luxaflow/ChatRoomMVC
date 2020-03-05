

class User(object):
    """
    Object voor gebruikerrs gegevens
    Momenteel geen noodzaak kunnen vinden voor meer dan een naam
    """
    def __init__(self, username):
        self.__username = username

    def get_username(self):
        return self.__username