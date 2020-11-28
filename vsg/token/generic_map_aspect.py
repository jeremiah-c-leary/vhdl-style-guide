
from vsg import parser


class generic_keyword(parser.keyword):
    '''
    unique_id = generic_map_aspect : generic_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class map_keyword(parser.keyword):
    '''
    unique_id = generic_map_aspect : map_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = generic_map_aspect : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = generic_map_aspect : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
