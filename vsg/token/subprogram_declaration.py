
from vsg import parser


class semicolon(parser.semicolon):
    '''
    unique_id = subprogram_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
