from datetime import datetime

class Log(object):

    """
    Logt wat er in de applicatie gebeurt naar ttext bestanden
    Maakt log bestanden aan wanneer deze nog niet bestaan
    """
    def __init__(self, log_name='main.log'):

        self.__file_path = './logs/{0}'.format(log_name)

        self.__file = open(self.__file_path, 'w')
        self.__file.close()


    """
    Past naam van log aan als de anders dient te worden
    Maakt bestand aan wanneer die nog niet bestaat
    """
    def set_log_name(self, log_name):

        self.__file_path = './logs/{0}'.format(log_name)

        self.__file = open(self.__file_path, 'w')
        self.__file.close()


    """
    Plaatst nieuw regel in een log
    """
    def write_log(self, message, msg_type='INFO'):

        time_stamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        file = open(self.__file_path, 'a')
        
        try:
            file.write('[{0}][{1}]: {2}\n'.format(time_stamp, msg_type, message))
        except IOError:
            print('Unable to write to file')   
        
        file.close()
