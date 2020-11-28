
from vsg import parser


class loop_label(parser.label):
    '''
    unique_id = loop_statement : loop_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = loop_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class loop_keyword(parser.keyword):
    '''
    unique_id = loop_statement : loop_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = loop_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_loop_keyword(parser.keyword):
    '''
    unique_id = loop_statement : end_loop_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_loop_label(parser.label):
    '''
    unique_id = loop_statement : end_loop_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = loop_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
