
from vsg import parser


class keyword(parser.keyword):
    '''
    unique_id = use_clause : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class selected_name(parser.selected_name):
    '''
    unique_id = use_clause : selected_name
    '''

    def __init__(self, sString):
        parser.selected_name.__init__(self, sString)


class comma(parser.comma):
    '''
    unique_id = use_clause : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class semicolon(parser.semicolon):
    '''
    unique_id = use_clause : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
