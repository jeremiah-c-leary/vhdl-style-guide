
from vsg import parser


class port_keyword(parser.keyword):
    '''
    unique_id = port_clause : port_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = port_clause : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = port_clause : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = port_clause : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
