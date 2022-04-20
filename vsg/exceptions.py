
class ClassifyError(Exception):
    '''
    Exception raised for errors when classifying VHDL Files.
    '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ConfigurationError(Exception):
    '''
    Exception raised for errors when configuration VSG..
    '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
