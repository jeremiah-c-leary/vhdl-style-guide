
from vsg import parser


class colon(parser.colon):
    '''
    unique_id = element_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = element_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
