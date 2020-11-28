
from vsg import parser


class array_keyword(parser.keyword):
    '''
    unique_id = unbounded_array_definition : array_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = unbounded_array_definition : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class comma(parser.comma):
    '''
    unique_id = unbounded_array_definition : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = unbounded_array_definition : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class of_keyword(parser.keyword):
    '''
    unique_id = unbounded_array_definition : of_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
