
from vsg import parser


class constant_keyword(parser.keyword):
    '''
    unique_id = interface_constant_declaration : constant_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = interface_constant_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = interface_constant_declaration : subtype_indication
    '''
    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = interface_constant_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class assignment(parser.assignment):
    '''
    unique_id = interface_constant_declaration : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
