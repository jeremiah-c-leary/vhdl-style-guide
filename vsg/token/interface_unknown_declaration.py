
from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = interface_unknown_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = interface_unknown_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class bus_keyword(parser.keyword):
    '''
    unique_id = interface_unknown_declaration : bus_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = interface_unknown_declaration : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
