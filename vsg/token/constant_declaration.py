
from vsg import parser


class constant_keyword(parser.keyword):
    '''
    unique_id = constant_declaration : constant_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = constant_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = constant_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = constant_declaration : subtype_indication
    '''

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = constant_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class assignment_operator(parser.item):
    '''
    unique_id = constant_declaration : assignment_operator
    '''

    def __init__(self, sString=':='):
        parser.item.__init__(self, ':=')
