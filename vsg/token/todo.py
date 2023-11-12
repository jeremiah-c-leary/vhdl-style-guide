
from vsg import parser


class name(parser.name):
    '''
    unique_id = todo : name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = todo : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = todo : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
