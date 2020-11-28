
from vsg import parser


class begin_keyword(parser.keyword):
    '''
    unique_id = generate_statement_body : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = generate_statement_body : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class alternative_label(parser.label):
    '''
    unique_id = generate_statement_body : alternative_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = generate_statement_body : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
