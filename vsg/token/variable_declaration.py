
from vsg import parser


class shared_keyword(parser.keyword):
    '''
    unique_id = variable_declaration : shared_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class variable_keyword(parser.keyword):
    '''
    unique_id = variable_declaration : variable_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = variable_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = variable_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class assignment_operator(parser.assignment):
    '''
    unique_id = variable_declaration : assignment_operator
    '''

    def __init__(self, sString=':='):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = variable_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
