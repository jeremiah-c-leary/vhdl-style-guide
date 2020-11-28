
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = type_declaration : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = type_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class type_definition(parser.item):
    '''
    unique_id = type_declaration : type_definition
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = type_declaration : semicolon
    '''

    def __init__(self):
        parser.semicolon.__init__(self)
