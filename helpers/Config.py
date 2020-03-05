

class Config(object):

    """
    Leest een .env bestand uit.
    In dit bestand zijn algemene waardes zoals host en port opgenomen
    """    
    def __init__(self, file='./.env'):

        self.__file = open(file, 'r')

        self.__content = None
        self._env = dict()

        try:
            # .env filteren van lege regels
            self.__content = [x for x in self.__file.read().split('\n') if x]
        except IOError:
            print('Error reading {0}'.format(file))

        self.__file.close()

        if self.__content:
            
            for line in self.__content:
                
                try:
                    key, value = line.split('=')
                except:
                    print('No = in line of data')
                    continue
                
                self._env[key] = value
