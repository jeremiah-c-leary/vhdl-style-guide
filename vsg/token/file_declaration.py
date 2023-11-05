
from vsg import parser


class file_keyword(parser.keyword):
    '''
    unique_id = file_declaration : file_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = file_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = file_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class identifier(parser.identifier):
    '''
    unique_id = file_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)
