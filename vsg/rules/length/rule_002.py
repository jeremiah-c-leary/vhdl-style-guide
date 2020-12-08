
from vsg.rules import file_length


class rule_002(file_length):
    '''
    Checks for length of the file.
    '''

    def __init__(self):
        file_length.__init__(self, 'length', '002')
