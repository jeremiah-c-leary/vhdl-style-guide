
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = library_clause : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = library_clause : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
