
from vsg import parser


class procedure_name(parser.item):
    '''
    unique_id = procedure_call : procedure_name
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = procedure_call : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = procedure_call : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
