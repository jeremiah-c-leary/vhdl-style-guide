
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


class keyword(parser.keyword):
    '''
    unique_id = variable_declaration : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = variable_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = variable_declaration : comma
    '''

    def __init__(self):
        parser.comma.__init__(self)


class colon(parser.colon):
    '''
    unique_id = variable_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class subtype_indication(parser.subtype_indication):
    '''
    unique_id = variable_declaration : subtype_indication
    '''

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class assignment_operator(parser.item):
    '''
    unique_id = variable_declaration : assignment_operator
    '''

    def __init__(self, sString=':='):
        parser.item.__init__(self, sString)


class assignment_expression(parser.item):
    '''
    unique_id = variable_declaration : assignment_expression
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = variable_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
