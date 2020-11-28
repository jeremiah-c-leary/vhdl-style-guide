
from vsg import parser


class case_label(parser.label):
    '''
    unique_id = case_statement : case_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = case_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class case_keyword(parser.keyword):
    '''
    unique_id = case_statement : case_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class question_mark(parser.question_mark):
    '''
    unique_id = case_statement : question_mark
    '''

    def __init__(self, sString='?'):
        parser.question_mark.__init__(self)


class is_keyword(parser.keyword):
    '''
    unique_id = case_statement : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = case_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_case_keyword(parser.keyword):
    '''
    unique_id = case_statement : end_case_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_case_label(parser.label):
    '''
    unique_id = case_statement : end_case_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = case_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
