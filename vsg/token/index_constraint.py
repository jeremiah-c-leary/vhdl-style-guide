
from vsg import parser


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = index_constraint : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class comma(parser.comma):
    '''
    unique_id = index_constraint : comma
    '''

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = index_constraint : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
