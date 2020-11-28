
from vsg import parser


class type_keyword(parser.keyword):
    '''
    unique_id = incomplete_type_declaration : type_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = incomplete_type_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = incomplete_type_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
