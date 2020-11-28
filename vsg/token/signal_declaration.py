
from vsg import parser


class signal_keyword(parser.keyword):
    '''
    unique_id = signal_declaration : signal_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class keyword(parser.keyword):
    '''
    unique_id = signal_declaration : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = signal_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = signal_declaration : comma
    '''

    def __init__(self):
        parser.comma.__init__(self)


class colon(parser.colon):
    '''
    unique_id = signal_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = signal_declaration : subtype_indication
    '''

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class assignment_operator(parser.assignment):
    '''
    unique_id = signal_declaration : assignment_operator
    '''

    def __init__(self, sString=':='):
        parser.assignment.__init__(self, ':=')


class assignment_expression(parser.item):
    '''
    unique_id = signal_declaration : assignment_expression
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = signal_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
