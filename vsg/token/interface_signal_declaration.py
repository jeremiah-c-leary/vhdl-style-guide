
from vsg import parser


class signal_keyword(parser.keyword):
    '''
    unique_id = interface_signal_declaration : signal_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = interface_signal_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = interface_signal_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class bus_keyword(parser.keyword):
    '''
    unique_id = interface_signal_declaration : bus_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = interface_signal_declaration : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
