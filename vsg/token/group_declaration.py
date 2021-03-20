
from vsg import parser


class group_keyword(parser.keyword):
    '''
    unique_id = group_declaration : group_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):
    '''
    unique_id = group_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):
    '''
    unique_id = group_declaration : colon
    '''

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class group_template_name(parser.name):
    '''
    unique_id = group_declaration : group_template_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = group_specification : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = group_specification : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = group_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
