
from vsg import parser


class for_keyword(parser.keyword):
    '''
    unique_id = timeout_clause : for_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
