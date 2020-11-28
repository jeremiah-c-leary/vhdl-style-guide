
from vsg import parser


class alternative_label_name(parser.label):
    '''
    unique_id = case_generate_alternative : alternative_label_name
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class alternative_label_colon(parser.label_colon):
    '''
    unique_id = case_generate_alternative : alternative_label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class when_keyword(parser.keyword):
    '''
    unique_id = case_generate_alternative : when_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = case_generate_alternative : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
