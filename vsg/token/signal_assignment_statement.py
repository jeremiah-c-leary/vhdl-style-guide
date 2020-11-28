
from vsg import parser


class label(parser.label):
    '''
    unique_id = signal_assignment_statement : label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.colon):
    '''
    unique_id = signal_assignment_statement : label_colon
    '''

    def __init__(self, sString=';'):
        parser.colon.__init__(self, sString)
