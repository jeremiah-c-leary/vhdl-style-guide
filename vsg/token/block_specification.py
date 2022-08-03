
from vsg import parser


class generate_statement_label(parser.label):
    '''
    unique_id = block_specification : generate_statement_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = block_specification : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = block_specification : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class architecture_name(parser.name):
    '''
    unique_id = block_specification : architecture_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
