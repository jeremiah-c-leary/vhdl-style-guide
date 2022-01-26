
from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = primary_unit_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = primary_unit_declaration : semicolon
    '''

    def __init__(self):
        parser.semicolon.__init__(self)
