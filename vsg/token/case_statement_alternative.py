
from vsg import parser


class when_keyword(parser.keyword):
    '''
    unique_id = case_statement_alternative : when_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = case_statement_alternative : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class others_keyword(parser.keyword):
    '''
    unique_id = case_statement_alternative : others_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
