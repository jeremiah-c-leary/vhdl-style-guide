
from vsg import parser


class on_keyword(parser.keyword):
    '''
    unique_id = sensitivity_clause : on_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
