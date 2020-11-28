
from vsg import parser


class attribute_keyword(parser.keyword):
    '''
    unique_id = attribute_declaration : attribute_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = attribute_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = attribute_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = attribute_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
