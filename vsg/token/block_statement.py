
from vsg import parser


class block_label(parser.label):
    '''
    unique_id = block_statement : block_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = block_statement : label_colon
    '''

    def __init__(self, sString=':'):
        parser.label_colon.__init__(self)


class block_keyword(parser.keyword):
    '''
    unique_id = block_statement : keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class guard_open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = block_statement : guard_open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class guard_condition(parser.item):
    '''
    unique_id = block_statement : guard_condition
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class guard_close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = block_statement : guard_close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class is_keyword(parser.keyword):
    '''
    unique_id = block_statement : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = block_statement : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = block_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_block_keyword(parser.keyword):
    '''
    unique_id = block_statement : end_block_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_block_label(parser.label):
    '''
    unique_id = block_statement : end_block_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = block_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
