
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


class comma(parser.comma):
    '''
    unique_id = interface_signal_declaration : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class colon(parser.colon):
    '''
    unique_id = interface_signal_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class mode_keyword(parser.keyword):
    '''
    unique_id = interface_signal_declaration : mode_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = interface_signal_declaration : subtype_indication
    '''

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


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


class static_expression(parser.static_expression):
    '''
    unique_id = interface_signal_declaration : static_expression
    '''

    def __init__(self, sString):
        parser.static_expression.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = interface_signal_declaration : semicolon
    '''

    def __init__(self):
        parser.semicolon.__init__(self)
