
from vsg import parser


class until_keyword(parser.keyword):
    '''
    unique_id = condition_clause : until_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
