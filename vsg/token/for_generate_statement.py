
from vsg import parser


class generate_label(parser.label):
    '''
    unique_id = for_generate_statement : generate_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = for_generate_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class for_keyword(parser.keyword):
    '''
    unique_id = for_generate_statement : for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class generate_keyword(parser.keyword):
    '''
    unique_id = for_generate_statement : generate_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = for_generate_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_generate_keyword(parser.keyword):
    '''
    unique_id = for_generate_statement : end_generate_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_generate_label(parser.label):
    '''
    unique_id = for_generate_statement : end_generate_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = for_generate_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
