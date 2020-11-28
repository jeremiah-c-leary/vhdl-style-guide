
from vsg import parser


class process_label(parser.label):
    '''
    unique_id = process_statement : process_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = process_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class postponed_keyword(parser.keyword):
    '''
    unique_id = process_statement : postponed_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class process_keyword(parser.keyword):
    '''
    unique_id = process_statement : process_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = process_statement : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = process_statement : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class is_keyword(parser.keyword):
    '''
    unique_id = process_statement : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = process_statement : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = process_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_postponed_keyword(parser.keyword):
    '''
    unique_id = process_statement : end_postponed_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_process_keyword(parser.keyword):
    '''
    unique_id = process_statement : end_process_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_process_label(parser.label):
    '''
    unique_id = process_statement : end_process_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = process_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
