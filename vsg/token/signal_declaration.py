
from vsg import parser


class signal_keyword(parser.keyword):
    '''
    unique_id = signal_declaration : signal_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = signal_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = signal_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class assignment_operator(parser.assignment):
    '''
    unique_id = signal_declaration : assignment_operator
    '''

    def __init__(self, sString=':='):
        parser.assignment.__init__(self, ':=')


class semicolon(parser.semicolon):
    '''
    unique_id = signal_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
