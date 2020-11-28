
from vsg import parser


class label(parser.label):
    '''
    unique_id = procedure_call_statement : label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = procedure_call_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = procedure_call_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
