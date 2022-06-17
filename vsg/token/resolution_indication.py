
from vsg import parser


class resolution_function_name(parser.name):
    '''
    unique_id = resolution_indication : resolution_function_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = resolution_indication : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = resolution_indication : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
